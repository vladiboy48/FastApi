## Тест коммита
import uvicorn
import os
from fastapi import FastAPI
from typing import Optional
from transform_json import json_to_dict_list, temp_json, delete_json
from base import reqDictn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
app = FastAPI()


@app.get("/persons")
def get_all_persons(pers_id: Optional[int] = None,
                    fio: Optional[str] = None,
                    login: Optional[str] = None,
                    password: Optional[str] = None,
                    role: Optional[str] = None
                    ):  # Optional, чтобы не обязательно былдо передавать параметр, но если да то инт нужен
    persons = reqDictn("Select * from persons")
    path_to_json = temp_json(persons, "temp_table_persons.txt")
    if (pers_id is None and fio is None and login is None and password is None and role is None):
        delete_json(path_to_json)
        return persons
    else:
        return_list = []
        for person in persons:
            if person['pers_id'] == pers_id:
                if person not in return_list:  # Проверка, чтобы не выводить одного и того же несколько раз
                    return_list.append(person)
        for person in persons:
            if person['fio'] == fio:
                if person not in return_list:
                    return_list.append(person)
        for person in persons:
            if person['login'] == login:
                if person not in return_list:
                    return_list.append(person)
        for person in persons:
            if person['password'] == password:
                if person not in return_list:
                    return_list.append(person)
        for person in persons:
            if person['role'] == role:
                if person not in return_list:
                    return_list.append(person)
        delete_json(path_to_json)
        return return_list


@app.get("/persons/{pers_id}")  # Отдельная страница пользователя с инфой
def get_one_person(pers_id: int):
    persons = reqDictn("Select * from persons")
    path_to_json = temp_json(persons, "temp_table_persons.txt")
    return_list = []
    for person in persons:
        if person['pers_id'] == pers_id:
            return_list.append(person)
    delete_json(path_to_json)
    return return_list
