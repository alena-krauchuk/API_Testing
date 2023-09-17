from src.my_requests import MyRequests


class TestCreateUsers:
    body = {
        "first_name": "Jim",
        "last_name": "Furry",
        "company_id": 1
    }

    def test_create_user(self):
        response = MyRequests.post(url="/users/", data=self.body)
        print(response.json())

















