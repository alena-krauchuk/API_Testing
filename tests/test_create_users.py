from src.my_requests import MyRequests
from generator.generator import generated_person
from src.assertions import Assertion
from data.status_code import StatusCode
from src.base_page import BasePage


class TestCreateUsers(BasePage):
    assertion = Assertion()
    status_code = StatusCode()
    keys = KeysCreateUser()


    def test_get_status_code_201(self, prepare_user_in_active_company):
        post_method = CreateUser()
        response = post_method.get_user(prepare_user_in_active_company)
        self.assertion.assert_status_code(response, self.status_code.CREATE)

    def test_create_user(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post(url="/users/", data=self.get_body(first_name, last_name, company_id))
        print(response.json())
        self.assertion.assert_first_name(response, first_name), "First name was not created"
        self.assertion.assert_last_name(response, last_name), "Last name was not created"


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
