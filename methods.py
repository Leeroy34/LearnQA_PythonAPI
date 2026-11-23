import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# 1. Запросы без параметра method

get_response = requests.get(url)
print("GET без параметра method:", get_response.text)

post_response = requests.post(url)
print("POST без параметра method:", post_response.text)

put_response = requests.put(url)
print("PUT без параметра method:", put_response.text)

delete_response = requests.delete(url)
print("DELETE без параметра method:", delete_response.text)

# 2. Запрос методом HEAD

head_response = requests.head(url)
print("HEAD статус:", head_response.status_code)
print("HEAD ответ:", head_response.text)

# 3. Запросы с правильным значением method

get_response = requests.get(url, params={"method": "GET"})
print("GET:", get_response.text)

post_response = requests.post(url, data={"method": "POST"})
print("POST:", post_response.text)

put_response = requests.put(url, data={"method": "PUT"})
print("PUT:", put_response.text)

delete_response = requests.delete(url, data={"method": "DELETE"})
print("DELETE:", delete_response.text)

# 4. Проверка всех сочетаний HTTP-методов

methods = ["GET", "POST", "PUT", "DELETE"]

for method in methods:
    if method == "GET":
        for parameter in methods:
            response = requests.get(url, params={"method": parameter})
            print(method, parameter, response.text)


    elif method == "POST":

        for parameter in methods:
            response = requests.post(url, data={"method": parameter})

            print(method, parameter, response.text)


    elif method == "PUT":

        for parameter in methods:
            response = requests.put(url, data={"method": parameter})

            print(method, parameter, response.text)


    elif method == "DELETE":

        for parameter in methods:
            response = requests.delete(url, data={"method": parameter})

            print(method, parameter, response.text)
