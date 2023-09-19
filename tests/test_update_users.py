from src.my_requests import MyRequests


class TestUpdateUsers:
    body = {
        "first_name": "Jim",
        "last_name": "Furry",
        "company_id": 1
    }

    def test_update_user(self):
        print(self.body.get("first_name"))
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json())
        print(response.json()["first_name"])
        print(response.status_code)


