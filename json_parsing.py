from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)


try:
    parsed_respose_text = response.json()
except JSONDecodeError:
    print('Ответ не в формате JSON')