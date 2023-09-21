from src.my_requests import MyRequests
from generator.generator import generated_person
from src.assertions import Assertion
from data.status_code import StatusCode


class TestCreateUsers:
    assertion = Assertion()
    status_code = StatusCode()

    # работает, но разбиваем надвое - def create_user(self) и def get_body(self, first_name, last_name, company_id)
    # позже осталось только def get_body, а генератор перенесли в def test_create_user(self)
    # def create_user_01(self):
    #     person_info = next(generated_person())
    #     first_name = person_info.first_name
    #     last_name = person_info.last_name
    #     company_id = person_info.company_id
    #     body = {
    #         "first_name": first_name,
    #         "last_name": last_name,
    #         "company_id": company_id
    #     }
    #     return body

    # работало и так, но после создания файла assertions.py переделали в след.ред.
    # def get_body(self, first_name, last_name, company_id):
    #     body = {
    #         "first_name": first_name,
    #         "last_name": last_name,
    #         "company_id": company_id
    #     }
    #     return body

    def get_body(self, first_name, last_name, company_id):
        body = {
            "first_name": first_name,
            "last_name": last_name,
            "company_id": company_id
        }
        return body

    def test_create_user(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post(url="/users/", data=self.get_body(first_name, last_name, company_id))
        print(response.json())
        body = response.json()
        assert body["first_name"] == first_name, "First name was not created"
        assert body["last_name"] == last_name, "Last name was not created"

    def test_get_status_code_201(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post(url="/users/", data=self.get_body(first_name, last_name, company_id))
        # assert response.status_code == 201, f"Status code isn't 201, status code is {response.status_code}" # меняем
        # self.assertion.assert_status_code(response, expected_status_code=201) # меняем на импорт status_code
        self.assertion.assert_status_code(response, self.status_code.CREATE)

    # ______________________________________________________________________________________
    # мой HW-тест 1 - теперь не работает
    def test_get_user_url(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.url)
        assert response.url == "https://send-request.me/api/users/"

    # мой HW-тест 2 - теперь не работает
    def test_get_user_first_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["first_name"])
        # assert response.json()["first_name"] == "Jim", "First name is incorrect"
        assert response.json()["first_name"] == self.body["first_name"], "First name is incorrect"

    # мой HW-тест 3 - теперь не работает
    def test_get_user_last_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["last_name"])
        assert response.json()["last_name"] == "Furry", "Last name is incorrect"
        # assert response.json()["last_name"] == self.body["last_name"], "Last name is incorrect"

    # мой HW-тест 4 - теперь не работает
    def test_get_user_company_id(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["company_id"])
        # assert response.json()["company_id"] == 1, "Company id is incorrect"
        assert response.json()["company_id"] == self.body["company_id"], "Company id is incorrect"

    # мой HW-тест 5 - теперь не работает
    def test_get_user_id(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["user_id"])
