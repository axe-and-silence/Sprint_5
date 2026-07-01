from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Кнопка "Вход и регистрация" на основной странице
        self.button_login_register = By.XPATH, ".//button[1]"

        # Кнопка "Нет аккаунта" на странице авторизации
        self.button_net_accaunta = By.CLASS_NAME, "buttonSecondary inButtonText undefined inButtonText"
        
        # Поле ввода "Введите Email" на странице авторизации
        self.email_field_authorization = By.NAME, 'email'

        # Поле ввода "Пароль" на странице авторизации
        self.password_field_authorization = By.NAME, 'password'

        # Кнопка "Войти" на странице авторизации
        self.button_of_login = By.XPATH, './/form/div[3]/button[1]'

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        self.avatar_of_user = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"

        # Имя пользователя на главной странице. Нужен для определения успешной авторизации
        self.name_of_user = By.CSS_SELECTOR, ".flexRow > div > h3" 

        # Кнопка "Выйти" на главной странице 
        self.button_of_logout = By.XPATH, ".//body/div/div/div[1]/div/div[1]/div/button"
    
    # Функция клика на кнопке "Вход и регистрация"    
    def click_login_registred(self):
        login_registred_button = self.driver.find_element(*self.button_login_register)
        login_registred_button.click()
    
    # Функция ввода существующего и валидного email
    def enter_email_field(self, email):
        username_field = self.driver.find_element(*self.email_field_authorization)
        username_field.send_keys(email)

    # Функция ввода валидного к email пароля
    def enter_password(self, password):
        password_field = self.driver.find_element(*self.password_field_authorization)
        password_field.send_keys(password)

    # Функция клика на кнопку "Войти"  
    def click_login(self):
        login_button = self.driver.find_element(*self.button_of_login)
        login_button.click()

    # Функция проверки наличия артефактов успешной авторизации
    def is_success_login(self):
        if self.avatar_of_user and self.name_of_user and '/login' in self.driver.current_url:
            return True

    # Функция проверки наличия артефактов успешной выхода из под пользователя
    def is_success_logout(self):
        if not (self.avatar_of_use and self.name_of_user) and self.button_login_register:
            return True     

    # Функция клика на кнопку "Выйти"  
    def click_logout_button(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, ".//div/div/div[1]/div/div[1]/div/button"))).click()

    # Функция прохождения всех этапов авторизации
    def login(self, email, password):
        self.click_login_registred()
        self.enter_email_field(email)
        self.enter_password(password)
        self.click_login()

    # Функция выхода из под пользователя
    def logout(self):
        self.click_logout_button()

    