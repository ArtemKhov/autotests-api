import socket # Импортируем модуль socket для работы с сетевыми соединениями


def server():
    # Создаем TCP-сокет (AF_INET - используем IPv4, SOCK_STREAM - задаем тип сокета как TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем TCP-сокет к адресу и порту
    server_address = ('localhost', 12345)
    server_socket.bind(server_address) # .bind() - связывает сокет с определенным IP-адресом и портом

    # Начинаем слушать входящие подключения (максимум 5 в очереди)
    server_socket.listen(5) # Если к серверу обратится более 5 клиентов одновременно, они будут ждать.
    print('Сервер запущен и ждет подключений на localhost:12345.')

    # Запускаем бесконечный цикл, чтобы сервер всегда ждал новые подключения
    while True:
        # Принимаем соединение от клиента
        client_socket, client_address = server_socket.accept()
        print(f'Подключение от {client_address}')

        # recv(1024) ждет и получает данные от клиента, максимум 1024 байта
        data = client_socket.recv(1024).decode() # .decode() — преобразует байты в строку (обычно в UTF-8)
        print(f'От клиента пришло: {data}')

        # Отправляем ответ клиенту
        # encode() — преобразует строку в байты, так как send() принимает только байты.
        response = f'Сервер получил: {data}'
        client_socket.send(response.encode())

        # Закрываем соединение с клиентом (только этого клиента, сам сервер продолжает работать)
        client_socket.close()


# проверяем, запущен ли файл напрямую отсюда, а не откуда-то из импорта
if __name__ == '__main__':
    server()