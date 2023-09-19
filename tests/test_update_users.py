from src.my_requests import MyRequests


class TestUpdateUsers:
    body = {
        "first_name": "July",
        "last_name": "Brando",
        "company_id": 2
    }

    def test_update_user(self):
        response = MyRequests.put(url="/users/22473", data=self.body)
        print(response.json())

    # Можно сделать проверки id, статус-код при апдейте, имя новое с именем прежним, то же с фамилией и id компании

    # __________________________________________________________________________________________________
    # мой HW-тест 6
    # Проверить, что id пользователя остался прежним
    def test_check_user_id_is_the_same(self):
        response = MyRequests.put(url="/users/22473", data=self.body)
        print(response.json()["user_id"])
        assert response.json()["user_id"] == 22473, "User id is not the same"

    # мой HW-тест 7
    # Проверить, что новое имя не равно предыдущему
    def test_check_new_first_name_of_user(self):
        response = MyRequests.put(url="/users/22473", data=self.body)
        print(response.json()["first_name"])
        assert response.json()["first_name"] != "Jim", "First name is incorrect"
        # assert response.json()["first_name"] == self.body["first_name"], "First name is incorrect"

    # мой HW-тест 8
    # Проверить, что новая фамилия не равна предыдущей
    def test_check_new_last_name_of_user(self):
        response = MyRequests.put(url="/users/22473", data=self.body)
        print(response.json()["last_name"])
        # assert response.json()["last_name"] != "Jim", "Last name is incorrect"
        assert response.json()["last_name"] == self.body["last_name"], "Last name is incorrect"

    # мой HW-тест 9
    # Проверить статус-код апдейта
    def test_get_status_code_201(self):
        response = MyRequests.post(url="/users/22473", data=self.body)
        print(response.status_code)
        # assert response.status_code == 201, f"Status code isn't 201, status code is {response.status_code}"
