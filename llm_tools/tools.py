from typing import List
from loguru import logger
from openai import OpenAI




def call_gpt_static(query: List[dict],
                    model: str = 'gpt-4-1106-preview',
                    temperature: float = 0.5):
    client = OpenAI(api_key=gpt_key, base_url=url)

    completion = client.chat.completions.create(
        model=model,
        messages=query,
        temperature=temperature,
        stream=False
    )
    prompt_tokens = completion.usage.prompt_tokens
    completion_tokens = completion.usage.completion_tokens
    total_tokens = completion.usage.total_tokens

    logger.info(
        f"prompt_tokens: {prompt_tokens}, completion_tokens: {completion_tokens}, total_tokens: {total_tokens}")
    # return completion.choices[0].message.content
    return {
        'content': completion.choices[0].message.content,
        'prompt_tokens': prompt_tokens,
        'completion_tokens': completion_tokens,
        'total_tokens': total_tokens
    }


def fix_json(json_string):
    """
    修复json字符串, Qwen有时候会少掉一个括号
    :param json_string:
    :return:
    """
    open_brackets = json_string.count('{')
    close_brackets = json_string.count('}')

    # 如果开括号比闭括号多，则尝试补全
    while open_brackets > close_brackets:
        json_string += '}'
        close_brackets += 1

    return json_string
