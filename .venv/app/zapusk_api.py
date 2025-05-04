# Нужен включенным уникорн, по сути тоже самое что и в постамане
import requests


def get_all_persons():
    url = "http://127.0.0.1:5000/persons"
    response = requests.get(url)
    return response.json()


def get_any_persons(pers_id):
    url = "http://127.0.0.1:5000/persons"
    response = requests.get(url, params={'pers_id': pers_id})
    return response.json()


persons = get_any_persons(pers_id=3)
for i in persons:
    print(i)

# persons = get_all_persons()
# for i in persons:
#     print(i)
