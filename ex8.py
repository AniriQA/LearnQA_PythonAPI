import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.text)
print(response.status_code)
response=time.sleep(10)
payload = {"token": "gM1ozM1oTMxACNx0CMx0SMyAjM"}
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params=payload)
print(response.text)
print(response.status_code)
if "result" in response.text:
    print("ответ содержит result")
else:
    print("ответ не содержит result")

