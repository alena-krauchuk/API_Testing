from src.my_requests import MyRequests


class TestDeleteUsers:

    def test_delete_users(self):
        response = MyRequests.delete(url="/users/22575")
        print(response.json())
        print(response.status_code)
        assert response.status_code == 202, f"Status code is not 202, status code is {response.status_code}"

    def test_delete_deleted_users(self):
        response = MyRequests.delete(url="/users/22575")
        print(response.json())
        print(response.status_code)
        assert response.status_code == 404, f"Status code is not 404, status code is {response.status_code}"









