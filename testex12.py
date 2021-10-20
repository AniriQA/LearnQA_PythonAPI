import requests
class Test:
    def test_check(self):
        URL = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(URL)
        print(dict(response.headers))
        q=response.headers
        assert response.status_code == 200
        assert response.headers == q
