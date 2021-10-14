import requests
list=['12345','123456789','qwerty','password','1234567','12345678','12345','iloveyou','111111','123123','abc123','qwerty123','q2w3e4r','admin','qwertyuiop','654321','555555','lovely','7777777','welcome','888888','princess','dragon','password1','123qwe']
for el in list:
    payload = {"login": "super_admin", "password": list}
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=payload)
    print(dict(response1.cookies))
    cookie_value=response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    print(response2.text)





