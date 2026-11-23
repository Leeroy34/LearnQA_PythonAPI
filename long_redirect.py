import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")
history = response.history

print(f"Кол-во редиректов: {len(history)}")
print(f"Финальный URL: {response.url}")