import os
import json


def temp_json(json_name, file_name):
    json_str = json.dumps(json_name, ensure_ascii=False)
    with open(file_name, 'w+', encoding='utf-8') as file:  # Создаём временный json
        file.write(json_str)
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Путь к директории текущего скрипта
    path_to_json = os.path.join(script_dir, file_name)  # Где лежит Json
    return path_to_json


def delete_json(path_to_json):
    os.remove(path_to_json)  # Удаляем временный json
    return 'ok'


def json_to_dict_list(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        json_str = file.read()
        dict_list = json.loads(json_str)
    return dict_list
