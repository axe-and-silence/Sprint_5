from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest

class RegistrationPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Кнопка "Вход и регистрация" на основной странице
        self.button_login_register = By.XPATH, ".//button[1]"

        # Кнопка "Нет аккаунта" на странице авторизации
        self.button_net_accaunta = By.XPATH, './/form/div[3]/button[2]'

        # Поле "Введите Email" на странице регистрации
        self.email_field_registration = By.NAME, 'email'

        # Поле ввода "Пароль" на странице регистрации
        self.password_field_registration = By.NAME, 'password'

        # Поле ввода "Повторите пароль" на странице регистрации
        self.repeat_password_field_registration = By.NAME, 'submitPassword'

        # Кнопка "Создать аккаунт" на форме регистрации
        self.button_of_registration =  By.XPATH, './/form/div[3]/button[1]'

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        self.avatar_of_user = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"

        # Имя пользователя на главной странице. Нужен для определения успешной авторизации
        self.name_of_user = By.CSS_SELECTOR, ".flexRow > div > h3"  

        # Красная рамка вокруг поля "Введите Email" на странице регистрации
        self.invalid_email_registred_email = './/div[2]/div[1]/div/div'

        # Красная рамка вокруг поля ввода "Пароль" на странице регистрации
        self.invalid_email_registred_password = './/div[2]/div[2]/div/div'

        # Красная рамка вокруг поля ввода "Повторите пароль" на странице регистрации
        self.invalid_email_registred_repeat_password = './/div[3]/div/div'

        # Красный текст "Ощибка" между полями "Введите Email" и "Пароль" на странице регистрации
        self.invalid_email_registred_error = './/div[1]/span'

    # Функция клика на кнопке "Вход и регистрация"    
    def click_login_registred(self):
        login_registred_button = self.driver.find_element(*self.button_login_register)
        login_registred_button.click()
    
    # Функция клика на кнопку "Нет аккаунта"    
    def click_button_net_accaunta(self):
        net_accaunta_button = self.driver.find_element(*self.button_net_accaunta)
        net_accaunta_button.click()
    
    # Функция ввода email на странице регистрации
    def enter_email_field_registration(self, email):
        username_field_registration = self.driver.find_element(*self.email_field_registration)
        username_field_registration.send_keys(email)
    
    # Функция ввода валидного пароля
    def enter_password_registration(self, password):
        password_field_registration = self.driver.find_element(*self.password_field_registration)
        password_field_registration.send_keys(password)
    
    # Функция ввода повтора пороля
    def enter_password_registration_repeat(self, password):
        password_field_registration_repeat = self.driver.find_element(*self.repeat_password_field_registration)
        password_field_registration_repeat.send_keys(password)

    # Функция клика на кнопку "Создать аккаунт"    
    def click_button_of_registration(self):
        button_of_registration = self.driver.find_element(*self.button_of_registration)
        button_of_registration.click()
    
    # Функция проверки наличия артефактов успешной авторизации
    def is_success_login(self):
        if self.avatar_of_user and self.name_of_user and '/login' in self.driver.current_url:
            return True
        
    # Функция проверки наличия артефактов неуспешной регистрации
    def is_unsuccess_registration(self):
        if self.invalid_email_registred_error and self.invalid_email_registred_password and self.invalid_email_registred_repeat_password and self.invalid_email_registred_email:
            return True

    # Функция прохождения всех этапов регистрации
    def registration(self, email, password):
        self.click_login_registred()
        self.click_button_net_accaunta()
        self.enter_email_field_registration(email)
        self.enter_password_registration(password)
        self.enter_password_registration_repeat(password)
        self.click_button_of_registration()