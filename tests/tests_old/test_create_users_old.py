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

    def test_get_status_code_201(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.status_code)
        assert response.status_code == 201, f"Status code isn't 201, status code is {response.status_code}"

    # мой HW-тест 1
    def test_get_user_url(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.url)
        assert response.url == "https://send-request.me/api/users/"

    # мой HW-тест 2
    def test_get_user_first_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["first_name"])
        # assert response.json()["first_name"] == "Jim", "First name is incorrect"
        assert response.json()["first_name"] == self.body["first_name"], "First name is incorrect"

    # мой HW-тест 3
    def test_get_user_last_name(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["last_name"])
        assert response.json()["last_name"] == "Furry", "Last name is incorrect"
        # assert response.json()["last_name"] == self.body["last_name"], "Last name is incorrect"

    # мой HW-тест 4
    def test_get_user_company_id(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["company_id"])
        # assert response.json()["company_id"] == 1, "Company id is incorrect"
        assert response.json()["company_id"] == self.body["company_id"], "Company id is incorrect"

    # мой HW-тест 5
    def test_get_user_id(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json()["user_id"])
