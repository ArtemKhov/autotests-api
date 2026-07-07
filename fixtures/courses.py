import pytest
from pydantic import BaseModel

from clients.courses.courses_client import CoursesClient, get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema, CreateCourseResponseSchema
from fixtures.files import FileFixture
from fixtures.users import UserFixture


class CourseFixture(BaseModel):
    """
    Представляет объект с данными созданного курса

    request: содержит данные запроса на создание курса (CreateCourseRequestSchema).
    response: содержит ответ API после создания курса (CreateCourseResponseSchema)
    """
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema


@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    """
    Cоздает клиент CoursesClient, который используется для взаимодействия с API курсов
    :param function_user: фикстура, предоставляющая тестового пользователя (UserFixture)
    :return: возвращает объект CoursesClient, уже аутентифицированный от имени данного пользователя
    """
    return get_courses_client(function_user.authentication_user)


@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FileFixture
) -> CourseFixture:
    """
    Cоздает подготовленный курс перед выполнением теста и возвращает объект с данными созданного курса

    :param courses_client: клиент для работы с API курсов (CoursesClient)
    :param function_user: пользователь, от имени которого создается курс (UserFixture)
    :param function_file: загруженный файл, который будет использоваться в качестве изображения превью курса
    :return: возвращается объект CourseFixture, содержащий запрос и ответ API
    """
    request = CreateCourseRequestSchema(
        preview_file_id=function_file.response.file.id,
        created_by_user_id=function_user.response.user.id
    )
    response = courses_client.create_course(request)
    return CourseFixture(request=request, response=response)
