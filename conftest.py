from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import random,string

# Фикстура на инициализацию драйвера
@pytest.fixture
def get_driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit() 
# Фикстура на ссылку на целевой сайт    
@pytest.fixture
def site(): 
    site = 'https://qa-desk.education-services.ru/'
    return site

# Фикстура на логин и пароль существующего пользователя
@pytest.fixture
def user():
    user.email = '123123@123123.ru',
    user.password = '123123'
    return user
# Фикстура на пароль нового пользователя
@pytest.fixture
def new_user_password():
    new_user_password = '123123'
    return new_user_password

# Фикстура на мыло нового пользователя, генерируемая 
@pytest.fixture
def new_user_email():
    # Определяем набор символов для локальной части (до @)
    chars = string.ascii_lowercase + string.digits  # Только буквы и цифры
    # Случайная длина имени пользователя от 5 до 10 символов
    username_length = random.randint(5, 10)
    # Генерируем случайное имя
    username = ''.join(random.choice(chars) for _ in range(username_length))
    # Гарантируем, что имя не начинается с цифры (по спецификации RFC)
    if username.isdigit():
        username = random.choice(string.ascii_lowercase) + username
    # Фиксированный домен
    domain = "@example.com"
    new_user_email = username + domain 
    return new_user_email

# Фикстура на невалидное мыло нового пользовтеля, генерируемая
@pytest.fixture
def new_user_invalid_email():
    # Определяем набор символов для локальной части (до @)
    chars = string.ascii_lowercase + string.digits  # Только буквы и цифры
    # Случайная длина имени пользователя от 5 до 10 символов
    username_length = random.randint(5, 10)
    # Генерируем случайное имя
    new_user_email = ''.join(random.choice(chars) for _ in range(username_length))
    return new_user_email

# Фикстура на новое объявление
@pytest.fixture
def advertisement():
    advertisement.name = 'Мопед',
    advertisement.description = 'Моторолер не мой!!! Я просто разместил ОБЪЯВУ'
    advertisement.cost = "2100"
    return advertisement