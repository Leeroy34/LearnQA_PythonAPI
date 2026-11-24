import requests
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = response.json()["token"]
seconds = response.json()["seconds"]

response_before_end = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token" : token})

if response_before_end.json()["status"] == "Job is NOT ready":
    print("Статус до завершения задачи отображается корректно")
else:
    print("Статус до завершения задачи неверный")

time.sleep(seconds)

response_with_correct_token = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token" : token})
result = response_with_correct_token.json()
status = response_with_correct_token.json()["status"]

if status == "Job is ready":
    print('Статус отображён корректно')
else:
    print('Статус неверный')

if "result" in result:
    print('Поле result отображается')
else:
    print('Поле result не отображается')