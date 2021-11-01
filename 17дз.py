import requests
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class Test17дз(BaseCase):
    def  test_get_user_details_not_auth(self):
        response = requests.get("https://playground.learnqa.ru/api/user/2")
        print(response.content)
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")
        new_name = "Cdfdfsfsf"
        response3 = requests.put(f"https://playground.learnqa.ru/api/user/2", data={"firstName": new_name})
        print(response3.content)
        Assertions.assert_code_status(response3, 400)

    def test_edit_just_created(self):
        #REGISTER
        register_date = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_date)
        Assertions.assert_code_status(response1,200)
        Assertions.assert_json_has_key(response1,'id')

        email = register_date['email']
        first_name = register_date['firstName']
        password = register_date['password']
        user_id = self.get_json_value(response1, 'id')

        #LOGIN
        login_data = {'email': email,'password': password}
        response2 = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "C"
        response3 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token},cookies={"auth_sid": auth_sid},data={"firstName": new_name})

        Assertions.assert_code_status(response3, 400)
        print(response3.text)

        # EDIT
        new_name = "Cdfdfsfsf"
        response3 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid}, data={"firstName": new_name})
        print(response3.content)
        Assertions.assert_code_status(response3, 200)


        #GET
        response4 = MyRequests.get(f"/user/{user_id}", headers={"x-csrf-token": token},cookies={"auth_sid": auth_sid})
        Assertions.assert_json_value_by_name(response4, "firstName", new_name, "wrong name of the user after edit")

        # EDIT
        email = "Cdfdfsfsf"
        response5 = MyRequests.put(f"/user/{user_id}", headers={"x-csrf-token": token},
                                   cookies={"auth_sid": auth_sid}, data={"email": email})
        print(response5.content)
        print(email)
        Assertions.assert_code_status(response5, 400)

