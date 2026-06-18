import httpx


# Проходим аутентификацию
login_payload = {
    "email": "user@example.com",
    "password": "string"
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)


# Инициализируем клиент
# позволяет управлять HTTP-соединениями и повторно использовать TCP-соединение между запросами
client = httpx.Client(
    base_url="http://localhost:8000",
    timeout=100,
    headers={"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
)

# Выполняем GET-запрос, используя клиент
# мы вызываем метод GET не у httpx напрямую, а через клиент
get_user_me_response = client.get("/api/v1/users/me")
get_user_me_response_data = get_user_me_response.json()

print('Get user me data:', get_user_me_response_data)