import socket # Импортируем модуль socket для работы с сетевыми соединениями


# Создаем TCP-сокет (AF_INET - используем IPv4, SOCK_STREAM - задаем тип сокета как TCP)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
server_address = ('localhost', 12345)
client_socket.connect(server_address) # .connect() — устанавливает TCP-соединение с сервером.

# Отправляем сообщение серверу
# .encode() — преобразует строку в байты, так как send() принимает только байты.
message = "Привет, сервер!"
client_socket.send(message.encode())

# Получаем ответ от сервера
# recv(1024) — получает максимум 1024 байта данных от сервера
response = client_socket.recv(1024).decode() # .decode() — преобразует байты в строку (обычно UTF-8)
print(f"Ответ от сервера: {response}")

# Закрываем соединение
client_socket.close()