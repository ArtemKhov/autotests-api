from enum import Enum


class APIRoutes(str, Enum):
    USERS = "/api/v1/users"
    FILES = "/api/v1/files"
    COURSES = "/api/v1/courses"
    EXERCISES = "/api/v1/exercises"
    AUTHENTICATION = "/api/v1/authentication"

    # преобразовывает элементы Enum в строку
    # позволяет избежать вывода лишней информации типа <APIRoutes.USERS: '/api/v1/users'>
    # будем сразу получать только эндпоинт типа /api/v1/users
    def __str__(self):
        return self.value