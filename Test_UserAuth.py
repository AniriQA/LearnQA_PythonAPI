import requests

class TestUserAuth:
    def test_auth_user(self):
        data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }

        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=data)
        assert "auth_sid" in response1.cookies, "Нет авторизованных куков"
        assert "x-csrf-token" in response1.headers, "Нет x-csrf-token в Header"
        assert "user_id" in response1.json(), "Нет user ID"

        auth_sid = response1.cookies.get("auth_sid")
        token = response1.headers.get("x-csrf-token")
        user_id_from_auth_metod = response1.json()['user_id']

        response2 = requests.get("https://playground.learnqa.ru/api/user/auth",
                                 headers={"x-csrf-token": token},
                                 cookies={"auth_sid": auth_sid})
        assert "user_id" in response2.json(), "user id не обнаружен во втором запросе"
        user_id_from_check_metod = response2.json()['user_id']
        assert user_id_from_auth_metod == user_id_from_check_metod, "id разные"
