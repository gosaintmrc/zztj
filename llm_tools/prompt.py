COUNT_NAMES_PROMPT = """
你是一个历史学家，下面是{file_name}的内容，请你帮我总结出在这些内容中出现了一些什么人名，他们分别出现了几次，他们的身份职位分别是什么，请以json格式返回给我。

你可以参考如下json返回格式：
[
    {{
        "name": "世宗孝武皇帝",
        "occurrences": 1,
        "position": "皇帝"
    }},
    {{
        "name": "庄助",
        "occurrences": 5,
        "position": "会稽庄助"
    }},
    {{
        "name": "卫绾",
        "occurrences": 3,
        "position": "丞相"
    }}
]

好的，现在开始！

内容：
{content}

输出：(请只要输出json内容，其他一概不要输出)
"""


COUNT_BACKGROUND_PROMPT = """
你是一个历史学家，下面是{file_name}的内容，请你帮我总结出在这些内容中出现的人物{name_list}，他们的的背景信息（任职皇帝时期，任职年份，能力大小，功绩等）和死亡状况（是否是非正常死亡，死亡原因）是什么，请如下示例的json格式返回给我。你可以根据这个内容进行总结，如果这个内容中没有出现，请你根据你自己的知识进行总结。

你可以参考如下json返回格式：
    {{
        "name": "萧何",
        "title": "丞相",
        "emperor": "汉高帝",
        "service_years": "前202年-前193年",
        "abilities": "政治才能极高",
        "achievements": "帮助刘邦统一天下，建立汉朝政权架构",
        "death_status": {{
            "normal_death": true,
            "cause": "自然死亡"
        }}
    }},
    {{
        "name": "周勃",
        "title": "丞相",
        "emperor": "汉景帝",
        "service_years": "前180年-前169年",
        "abilities": "军事、政治双全",
        "achievements": "平定吕后政变，恢复汉室威信",
        "death_status": {{
            "normal_death": false,
            "cause": "被迫自杀"
        }}
    }}

好的，现在开始！

内容：
{content}

输出：(请只要输出json内容，其他一概不要输出)
"""