import sys
import platform

from config import settings


def create_allure_environment_file():
    # Создаем список из элементов в формате {key}={value}
    # загруженные изображения / url / таймауты и тд
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    # Добавляем информацию на какой ОС запускали автотесты
    items.append(f'os_info={platform.system()}, {platform.release()}')
    # Добавляем информацию на какой версии python запускались
    items.append(f'python_version={sys.version}')
    # Собираем все элементы в единую строку с переносами
    properties = '\n'.join(items)

    # Открываем файл ./allure-results/environment.properties на запись
    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)  # Записываем переменные в файл
