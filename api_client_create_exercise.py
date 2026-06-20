from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.files.files_client import get_files_client, CreateFileRequestDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email


# Инициализируем клиент public_users_client для работы с пользователями
public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
# Отправляем запрос и сохраняем ответ, чтобы далее использовать созданного пользователя
create_user_response = public_users_client.create_user(create_user_request)

# Инициализируем клиента authentication_user с email и паролем нового пользователя
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)
# Инициализируем files_client, который будет использоваться для загрузки файлов.
files_client = get_files_client(authentication_user)
# Инициализируем courses_client, который нужен для работы с курсами
courses_client = get_courses_client(authentication_user)
# Инициализируем exercises_client, который нужен для работы с заданиями
exercises_client = get_exercises_client(authentication_user)

# Загружаем файл
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
# Отправляем запрос на загрузку файла
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response) # Выводим в консоль данные о загруженном файле

# Создаем курс
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)


# Создаем задание на основе курса
create_exercise_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
