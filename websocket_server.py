import asyncio # Импортируем asyncio для работы с асинхронными операциями

import websockets # Импортируем библиотеку для работы с WebSockets
from websockets import ServerConnection # объект соединения с клиентом


# Обработчик входящих сообщений:
# Функция echo бесконечно читает сообщения от клиента
# Если клиент присылает новое сообщение, оно сразу обрабатывается
# Сервер отвечает клиенту на каждое сообщение.
async def echo(websocket: ServerConnection):
    async for message in websocket: # Асинхронно обрабатываем входящие сообщения
        print(f'Сообщение получено: {message}') # Логируем полученное сообщение
        response = f'Сервер получил: {message}' # Формируем ответное сообщение
        await websocket.send(response) # Отправляем ответ клиенту


# Запуск WebSocket-сервера на порту 8765
async def main():
    # Запускаем сервер (используем echo в качестве обработчика сообщений)
    server = await websockets.serve(echo, "localhost", 8765)
    # Выводим сообщение о запуске
    print('WebSocket сервер запущен на ws://localhost:8765')

    await server.wait_closed() # Ожидаем закрытия сервера (обычно он работает вечно)


# запускаем main(), который создаёт сервер и удерживает его в рабочем состоянии
asyncio.run(main())