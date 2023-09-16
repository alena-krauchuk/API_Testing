from pprint import pprint

import pytest
from data.data_files import StatusCompanies
from src.my_requests import MyRequests


class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()

    @pytest.mark.parametrize("status", status_list)
    def test_get_statuses_companies(self, status):
        # response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        response = self.request.get(f"?status={status}&limit=3&offset=0")
        print()
        # получаем json
        pprint(response.json())
        # проверяем хедеры
        pprint(response.headers)
        # pprint(response.status_code)
        # pprint(response.encoding)
        assert response.status_code == 200, f"Status code is not 200, status code is {response.status_code}"

    @pytest.mark.parametrize("status", status_list)
    def test_get_closed_companies(self, status):
        # response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        response = self.request.get(f"/?status={status}&limit=3&offset=0")
        # print(response.json()["data"])
        # print(response.json()["data"][0])
        # print(response.json()["data"][0]["company_status"])
        items_list = response.json()["data"]
        print(items_list)
        # можно сделать так:
        # здесь в принтах проверяем, что в ответе на запрос возвращен тот же статус, который был передан в response
        for item in range(len(items_list)):
            print(items_list[item]["company_status"])
            print(status)
            assert items_list[item]["company_status"] == status
        #     или
        # for item in items_list:
        #     assert item["company_status"] == status

    # ______________________________________________________________________
    # HW_test_01
    @pytest.mark.parametrize("status", status_list)
    def test_get_encoding_of_companies_data(self, status):
        # response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        response = self.request.get(f"?status={status}&limit=3&offset=0")
        print()
        pprint(response.json())         # получаем json
        pprint(response.encoding)       # проверяем encoding
        assert response.encoding == 'utf-8', f"Encoding is not 'utf-8', encoding is {response.encoding}"









