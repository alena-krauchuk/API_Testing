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

    # Проверить, что новое первое имя не равно предыдущему
    def test_check_new_first_name_of_user(self):
        response = MyRequests.put(url="/users/22473", data=self.body)
        print(response.json()["first_name"])
        assert response.json()["first_name"] != "Jim", "First name is incorrect"
        # assert response.json()["first_name"] == self.body["first_name"], "First name is incorrect"

















