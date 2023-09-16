import pytest
import requests
from pprint import pprint

base_url = "https://send-request.me/api/companies"


# 1
# Получение json

# самый простой запрос на получение json всех компаний
def test_get_companies():
    response = requests.get(base_url)
    pprint(response.json())


# запрос на получение json активных компаний с f-строкой и pprint библиотекой
def test_get_active_companies():
    response = requests.get(f"""{base_url}/?status=ACTIVE""")
    print()
    pprint(response.json())


# запрос на получение json активных компаний с f-строкой и pprint библиотекой,
# ограничением выдачи по количеству елементов limit
# и указанием начального порядкового номера (по умолчанию = 0) offset
def test_get_active_companies_01():
    response = requests.get(f"""{base_url}/?status=ACTIVE&limit=3&offset=0""")
    print()
    pprint(response.json())


# запрос на получение json закрытых компаний с f-строкой и pprint библиотекой,
# ограничением выдачи по количеству елементов limit
# и указанием начального порядкового номера (по умолчанию = 0) offset
def test_get_closed_companies():
    response = requests.get(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
    print()
    pprint(response.json())


# запрос на получение json компаний-банкротов с f-строкой и pprint библиотекой,
# ограничением выдачи по количеству елементов limit
# и указанием начального порядкового номера (по умолчанию = 0) offset
def test_get_bankrupt_companies():
    response = requests.get(f"""{base_url}/?status=BANKRUPT&limit=3&offset=0""")
    print()
    pprint(response.json())


# ________________________________________________________________________________
# 2
# Получение status code

# запрос на получение статус кода закрытых компаний с f-строкой, pprint библиотекой,ограничением limit и началом offset
def test_get_closed_companies_01():
    response = requests.get(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
    print()
    pprint(response.status_code)


# ________________________________________________________________________________
# 3
# Получение урла

# запрос на получение урла закрытых компаний с f-строкой, pprint библиотекой,ограничением limit и началом offset
def test_get_closed_companies_02():
    response = requests.get(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
    print()
    pprint(response.url)


# ________________________________________________________________________________
# 4
# Получение хедеров

# запрос на получение хедеров закрытых компаний с f-строкой, pprint библиотекой,ограничением limit и началом offset
def test_get_closed_companies_03():
    response = requests.get(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
    print()
    pprint(response.headers)


# ________________________________________________________________________
# 5
# Проверки через assert (как и нужно делать в pytest)


# запрос на выполнение через assert проверки статус-кода для закрытых компаний
def test_get_closed_companies_04():
    response = requests.get(f"""{base_url}/?status=CLOSED&limit=3&offset=0""")
    assert response.status_code == 200, f"Status code is not 200, status code is {response.status_code}"


# _______________________________________________________________________
# 6
# запрос на выполнение через assert проверки статус-кода для любых компаний
# этот один тест можно запускать один вместо трех предыдущих - для active, bankrupt и closed компаний

status_list = ["ACTIVE", "BANKRUPT", "CLOSED"]


@pytest.mark.parametrize("status", status_list)
def test_get_statuses_companies(status):
    response = requests.get(f"""{base_url}/?status={status}&limit=3&offset=0""")
    assert response.status_code == 200, f"Status code is not 200, status code is {response.status_code}"

# можно сделать проверки на наличие ключей, значений этих ключей
# можно модифицировать эти проверки, получать нужные значения


# Теперь оформим перенос данных в отдельные файлы
