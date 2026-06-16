import httpx


try:
    response = httpx.get("https://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid-url")
    response.raise_for_status()  # Вызовет исключение при 4xx/5xx
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")


client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
response = client.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2")
print(response.json())  # Заголовки включены в ответ
client.close()


with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи


files = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://postman-echo.com/post", files=files)
print(response.json())  # Ответ с данными о загруженном файле


params = {"userId": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач


headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://postman-echo.com/get?foo1=bar1&foo2=bar2", headers=headers)
print(response.json())
print(response.request.headers)


data = {"username": "test_user", "password": "123456"}
response = httpx.post("https://postman-echo.com/post", data=data)
print(response.json())


data = {
    "title": "Новая задача",
    "completed": False,
    "userId": 1
}
# json=<передаем_наш_json>
response = httpx.post('https://jsonplaceholder.typicode.com/todos', json=data)
print(response.status_code) # получаем код ответа
print(response.json()) # получаем JSON-ответ


response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
print(response.status_code) # получаем код ответа
print(response.json()) # получаем JSON-ответ



