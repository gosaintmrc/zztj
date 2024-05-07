import json

from loguru import logger

from llm_tools.prompt import COUNT_NAMES_PROMPT
from llm_tools.tools import call_gpt_static, fix_json


def count_name_position(content: dict):
    for key, value in content.items():
        file_name = key
        content = value
        # print("file_name: ", file_name)
        # print("content: ", content)

        llm_content = COUNT_NAMES_PROMPT.format(file_name=file_name, content=content)
        print(llm_content)

        result = call_gpt_static(
            query=[{"role": "user", "content": llm_content}],
            model='gpt-4-1106-preview', temperature=0.5)["content"]

        # 提取JSON内容并转换格式
        bracket_index = result.find('{')
        bracket_last = result.rfind('}')
        result = result[bracket_index:bracket_last + 1]
        result_content = fix_json(result)

        logger.info(file_name + "*OUTPUT*: " + result_content)

        result_content_json = json.loads(result_content)

        with open(f"name-position-occurrences/{file_name}.json", "w", encoding="utf-8") as f:
            json.dump(result_content_json, f, ensure_ascii=False, indent=4)

        logger.info(f"Saved {file_name}.json")


# Call the function
def main():
    with open("zztj_content.json", "r", encoding="utf-8") as f:
        content = json.load(f)

    count_name_position(content)


if __name__ == "__main__":
    main()
