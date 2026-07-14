from enum import Enum


class AllureEpic(str, Enum):
    """
    Cистема состоит из трёх основных частей:
    LMS (система управления обучением),
    Система для студентов,
    Система администрирования.
    """
    LMS = "LMS service"
    STUDENT = "Student service"
    ADMINISTRATION = "Administration service"