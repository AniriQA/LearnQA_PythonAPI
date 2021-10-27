
import requests

from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
class TestUserRegister(BaseCase):
   


    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = {'password': '123', 'username': "laernga", 'firstName': "learnqa", 'lastName': "learnqa", 'email': email}
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        print(response.status_code)
        print(response.content)
        assert response.status_code == 400, f'статус код {response.status_code}'