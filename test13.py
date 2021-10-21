import pytest
import requests
class Test13:
    header = [('Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'),('Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'),('Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'),('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'),('Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1')]
    @pytest.mark.parametrize('header',header)
    def test(self,header):
        URL = 'https://playground.learnqa.ru/ajax/api/user_agent_check'
        headers = {"User-Agent": header}
        response = requests.get(URL, headers)
        if "'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30'" in "user_agent":
            assert  "'platform': 'Mobile', 'browser': 'No', 'device': 'Android'" in response.text, "Тест не прошел"
        elif "'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1'" in "user_agent":
            assert "'platform': 'Mobile', 'browser': 'Chrome', 'device': 'iOS'" in response.text, "Тест не прошел"
        elif "'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'" in "user_agent":
            assert "'platform': 'Googlebot', 'browser': 'Unknown', 'device': 'Unknown'" in response.text, "Тест не прошел"
        elif "'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0'" in "user_agent":
            assert "'platform': 'Web', 'browser': 'Chrome', 'device': 'No'" in response.text, "Тест не прошел"
        elif "'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'" in "user_agent":
            assert "'platform': 'Mobile', 'browser': 'No', 'device': 'iPhone'" in response.text, "Тест не прошел"


