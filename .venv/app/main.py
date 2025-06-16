## Тест коммита
import uvicorn
import os
from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse,FileResponse,HTMLResponse
from typing import Optional
from transform_json import json_to_dict_list, temp_json, delete_json
from base import reqDictn, reqSimp

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=5000, log_level="info")
app = FastAPI()


@app.get("/persons") #общий эндопоинт в котором прописаны все фильтры
def get_all_persons(pers_id: Optional[int] = None,
                    fio: Optional[str] = None,
                    login: Optional[str] = None,
                    password: Optional[str] = None,
                    role: Optional[str] = None
                    ):
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

@app.post("/persons/admins")  # Лист админов.
def get_admins_list():
    persons = reqDictn("""Select * from persons where role = 'admin'""")
    path_to_json = temp_json(persons, "temp_table_persons.txt")
    return_list = []
    for person in persons:
        return_list.append(person)
    delete_json(path_to_json)
    return return_list

@app.post("/insert_person") # Добавление пользователя через тело пост запроса
def add_new_person(data=Body()): #Body задаётся через свагер в виде json - ниже парсим его в переменные и инсертим в БД
    fio = data["fio"]
    login = data["login"]
    pwd = data["password"]
    try:
        script = ("""insert into public.persons (fio,login,password) values ('%s', '%s', '%s');""" % (fio, login, pwd))
        reqSimp(script)
    except Exception as owibka:
        reg_status = ('--Задайте другой логин -, такой уже существует--')
    else:
        reg_status = ('Регистрация прошла успешно!')
    return reg_status

@app.delete("/delete_person") #Удаление пользовователя через тело пост запроса
def delete_person(data=Body()):
    enter_login = data["enter_login"]
    script = ("""delete from public.persons where login like '%s';""" % (enter_login))
    reqSimp(script)
    del_result = 'Удаление прошло успешно!'
    return del_result

@app.delete("/delete_person/{enter_login}") #Удаление пользовователя - логин передаём в прямо в пути
def delete_person(enter_login):
    try:
        script = ("""delete from public.persons where login like '%s';""" % (enter_login))
        reqSimp(script)
    except Exception as owibka:
        del_result = '--Задайте другой логин - такого пользователя не существует!--'
    else:
        del_result = 'Удаление прошло успешно!'
    return del_result
