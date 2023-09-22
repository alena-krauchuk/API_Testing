import requests
from requests import Response


class Assertion:

    # проверка совпадения фактического статус-кода с ожидаемым
    def assert_status_code(self, response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}, Actual: {actual_status_code}"

        # проверка совпадения фактического статус-кода с ожидаемым
    def assert_text(self, actual_text: str, expected_text: str):
        assert actual_text == expected_text, "Text is not equal"

    # проверка совпадения фактического текста из полученного ответа с ожидаемым
    def assert_body_text(self, actual_text: str, expected_text: str):
        assert actual_text == expected_text, "Text is not equal"

    # проверка совпадения фактического имени из полученного ответа с ожидаемым (коммент в ассерте - мой)
    def assert_first_name(self, response: Response, expected_text: str):
        actual_text = response.json()
        assert actual_text["first_name"] == expected_text, \
            f"Unexpected text. Expected: {expected_text}, Actual: {actual_text}"

    # проверка совпадения фактической фамилии из полученного ответа с ожидаемой (коммент в ассерте - мой)
    def assert_last_name(self, response: Response, expected_text: str):
        actual_text = response.json()
        assert actual_text["last_name"] == expected_text, \
            f"Unexpected text. Expected: {expected_text}, Actual: {actual_text}"
