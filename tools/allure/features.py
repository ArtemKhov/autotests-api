from enum import Enum


class AllureFeature(str, Enum):
    """
    Ключевые фичи системы:
    пользователи, файлы, курсы, задания и аутентификация.
    """
    USERS = "Users"
    FILES = "Files"
    COURSES = "Courses"
    EXERCISES = "Exercises"
    AUTHENTICATION = "Authentication"