from src.my_requests import MyRequests


class TestDeleteUsers:

    def test_delete_users(self):
        response = MyRequests.delete(url="/users/22573")
        print(response.json())
        print(response.status_code)
        assert response.status_code == 202, "User id is not the same"


