import pytest
from pydantic import BaseModel

from clients.files.files_client import get_files_client, FilesClient
from clients.files.files_schema import CreateFileRequestSchema, CreateFileResponseSchema
from fixtures.users import UserFixture


class FileFixture(BaseModel):
    """
    Вспомогательный класс

    request: данные запроса на загрузку файла (CreateFileRequestSchema)
    response: ответ от API после успешного создания файла (CreateFileResponseSchema)
    """
    request: CreateFileRequestSchema
    response: CreateFileResponseSchema


@pytest.fixture
def files_client(function_user: UserFixture) -> FilesClient:
    """
    Создает клиент FilesClient, который будет использоваться для работы с API загрузки файлов

    :param function_user: пользователь, полученный через фикстуру UserFixture
    :return: возвращает объект FilesClient
    """
    return get_files_client(function_user.authentication_user)


@pytest.fixture
def function_file(files_client: FilesClient) -> FileFixture:
    """
    Автоматически создает тестовый файл перед каждым тестом и возвращает информацию о нем
    При вызове function_file в тестах уже будет готовый загруженный файл

    :param files_client: отправляет запрос в API, загружая файл
    :return: возвращается объект FileFixture, содержащий данные запроса и ответа API
    """
    request = CreateFileRequestSchema(upload_file="./testdata/files/image.png")
    response = files_client.create_file(request)
    return FileFixture(request=request, response=response)

