from src.my_requests import MyRequests


class TestUpdateUsers:
    body = {
        "first_name": "Jim",
        "last_name": "Furry",
        "company_id": 2
    }

    def test_update_user(self):
        response = MyRequests.put(url="/users/22473", data=self.body)
        print(response.json())
















