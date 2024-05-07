import os
import re
import json


def remove_html_tags(text):
    # 使用正则表达式移除HTML标签
    clean_text = re.sub(r'<[^>]+>', '', text)
    return clean_text


def read_files_in_directory(directory):
    # 用于存储文件内容的暂时字典，键为文件初始文件名，值为文件内容
    temp_dict = {}

    # 遍历目录中的所有文件
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                content = remove_html_tags(content)
                temp_dict[filename] = content

    # 重新构建字典，键格式为"资治通鉴第九卷-汉纪一"，并按照文件名前的数字排序
    sorted_dict = {}
    for key in sorted(temp_dict, key=lambda x: int(x.split('-')[0])):
        # 移除'.md'并提取中间的文本作为新键
        new_key = '-'.join(key.split('-')[1:])  # 抽取除第一部分数字和.md外的内容
        new_key = new_key.rstrip('.md')  # 移除尾部的.md
        sorted_dict[new_key] = temp_dict[key]

    return sorted_dict


def save_dict_as_json(content_dict, file_path):
    # 将字典保存为JSON文件
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(content_dict, file, ensure_ascii=False, indent=4)


# 指定目录
directory_path = '/Users/tuozhou/Desktop/My_PhD/Quantitative_History/zztj/C-汉纪'
# 调用函数读取文件
hanji_contents = read_files_in_directory(directory_path)

# 将内容保存为JSON文件
json_file_path = '/Users/tuozhou/Desktop/My_PhD/Quantitative_History/zztj/llm_tools/zztj_content.json'
save_dict_as_json(hanji_contents, json_file_path)

# 如果需要查看某个特定的条目，可以直接访问
print(hanji_contents['资治通鉴第九卷-汉纪一'])  # 根据新的键查看内容