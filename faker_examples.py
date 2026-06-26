# импортируем класс Faker
from faker import Faker


# создаем объект класса Faker
fake = Faker()
print(fake.name())         # Выведет: John Doe
print(fake.address())      # Выведет: 1234 Elm St, Springfield, IL
print(fake.email())        # Выведет: j.doe@example.com

print()

# Генерация фейковых данных в определенной локализации
fake = Faker('ru_RU')
print(fake.name())         # Выведет: Иван Иванов
print(fake.address())      # Выведет: ул. Пушкина, дом 10

print()

# Генерация нескольких данных за один раз
fake = Faker()
# для одного юзера сразу создаются фейковые Имя, имейл, адресс
user_data = {
    "name": fake.name(),
    "email": fake.email(),
    "address": fake.address()
}
print(user_data)