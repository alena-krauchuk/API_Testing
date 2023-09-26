from data.urls import Urls
from generator.generator import generated_person
from src.base_page import BasePage
from src.my_requests import MyRequests


class UpdateUser(BasePage):
    url = Urls()

    def update_first_name(self, response):
        print(response.json())
        first_name_before = response.json()["first_name"]
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = response.json()["last_name"]
        company_id = response.json()["company_id"]
        user_id = response.json()["user_id"]
        print(first_name, last_name, company_id, user_id)
        body = self.prepare_creating_data(first_name=first_name, last_name=last_name, company_id=company_id)
        print(body)
        url = f"{self.url.create_user}{user_id}"
        print(url)
        response = MyRequests.put(url, body)
        return response, first_name_before
