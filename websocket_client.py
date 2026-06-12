import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес WebSocket-сервера
    # Используем async with, чтобы соединение автоматически закрылось после завершения работы клиента
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"  # Сообщение от клиента
        print(f"Отправка: {message}")
        await websocket.send(message)  # Асинхронно отправляем сообщение клиента серверу

        response = await websocket.recv()  # Асинхронно получаем ответ от сервера
        print(f"Ответ от сервера: {response}") # Логируем полученный ответ


# Запускаем асинхронную функцию клиента
asyncio.run(client())