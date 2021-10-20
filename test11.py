import requests
class Test:
    def test_check(self):
        URL = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(URL)
        assert response.status_code == 200
        assert dict(response.cookies) == {'HomeWork': 'hw_value'}



