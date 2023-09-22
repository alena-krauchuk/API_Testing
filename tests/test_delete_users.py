from src.my_requests import MyRequests
from src.assertions import Assertion
from data.status_code import StatusCode


class TestDeleteUsers:
    assertion = Assertion()
    status_code = StatusCode()

    def test_delete_users(self):
        response = MyRequests.delete(url="/users/22852")
        # print(response.text)
        # assert response.status_code == 202, f"Status code is not 202, status code is {response.status_code}"
        self.assertion.assert_status_code(response, self.status_code.ACTUAL)

    def test_delete_users_has_text_null(self):
        response = MyRequests.delete(url="/users/22883")
        print(response.text)
        # assert response.text == "null", "Wrong text"
        actual_text = response.text
        self.assertion.assert_text(actual_text, expected_text="null")

    def test_delete_deleted_users_has_status_code_404(self):
        response = MyRequests.delete(url="/users/22578")
        # assert response.status_code == 404, f"Status code is not 404, status code is {response.status_code}"
        self.assertion.assert_status_code(response, self.status_code.NOT_FOUND)

    def test_delete_deleted_users_has_text(self):
        response = MyRequests.delete(url="/users/22583")
        # assert response.json()["detail"]["reason"] == "User with requested id: 22576 is absent", "Wrong text"
        actual_text = response.json()["detail"]["reason"]
        self.assertion.assert_text(actual_text, expected_text="User with requested id: 22583 is absent")









