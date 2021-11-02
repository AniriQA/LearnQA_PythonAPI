
from lib.my_requests import MyRequests

from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
class TestUserRegister(BaseCase):
    def setup(self):
        base_part = 'learnqa'
        domain = 'example.com'
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
    def test_create_user_successfully(self):
        data = {'password': '123', 'username': "laernga", 'firstName': "learnqa", 'lastName': "learnqa", 'email': self.email}
        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, 'id')
    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = {'password': '123', 'username': "laernga", 'firstName': "learnqa", 'lastName': "learnqa", 'email': email}
        response =  MyRequests.post("/user/", data=data)
        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response,400)

    def test_create_user_with_existing_email_1(self):
            email = "vinkotovexample.com"
            data = {'password': '123', 'username': "laernga", 'firstName': "learnqa", 'lastName': "learnqa",
                    'email': email}
            response = MyRequests.post("/user/", data=data)
            print(response.status_code)
            print(response.content)
            Assertions.assert_code_status(response, 400)
    def test_create_user_with_existing_email_2(self):
        email = "vinkotov@example.com"
        data = {'password': '123', 'username': "q", 'firstName': "learnqa", 'lastName': "learnqa", 'email': email}
        response =  MyRequests.post("/user/", data=data)
        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response,400)

    def test_create_user_with_existing_email(self):
        email = "vinkotov@example.com"
        data = {'password': '123', 'username': "pytest конструирует строку, которая является идентификатором (ID) теста для каждого множества значений параметризованного теста. Эти индентификаторы можно использовать с опцией -k, чтобы отборать для выполнения определенные тесты, и они же идентифицируют конкретный упавший тест. Запустив pytest --collect-only , можно посмотреть сгенерированные ID.", 'firstName': "learnqa", 'lastName': "learnqa", 'email': email}
        response =  MyRequests.post("/user/", data=data)
        print(response.status_code)
        print(response.content)
        Assertions.assert_code_status(response, 400)
