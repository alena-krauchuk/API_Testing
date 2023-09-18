from src.my_requests import MyRequests


class TestCreateUsers:
    body = {
        "first_name": "Jim",
        "last_name": "Furry",
        "company_id": 1
    }

    def test_create_user(self):
        print(self.body.get("first_name"))
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json())
        print(response.json()["first_name"])
        print(response.status_code)
        print(response.url)  # мое

    # мой HW-тест 1
    def test_get_user_url(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.url)
        assert response.url == "https://send-request.me/api/users/"


    # мой HW-тест 2
    def test_get_user_first_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["first_name"])
        # assert response.json()["first_name"] == "Jim"
        assert response.json()["first_name"] == self.body["first_name"]

    # мой HW-тест 3
    def test_get_user_last_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["last_name"])
        assert response.json()["last_name"] == "Furry"
        # assert response.json()["last_name"] == self.body["last_name"]


