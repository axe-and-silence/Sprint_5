from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from locators.login_pages_locators import LoginPageLocators


class LoginPage(BasePage):
    

    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.go_to_page()
                 
    # Функция клика на кнопке "Вход и регистрация"    
    def click_login_registred(self):
        self.click_element(LoginPageLocators.BUTTON_LOGIN_REGISTER)
    
    # Функция ввода существующего и валидного email
    def enter_email_field(self, username: str):
        self.enter_text(LoginPageLocators.EMAIL_FIELD_AUTHORIZATION, username)

    # Функция ввода валидного к email пароля
    def enter_password(self, password: str):
        self.enter_text(LoginPageLocators.PASSWORD_FIELD_AUTHORIZATION, password)
    
    # Функция клика на кнопку "Войти"  
    def click_login(self):
        self.click_element(LoginPageLocators.BUTTON_OF_LOGIN)

    # Функция проверки наличия артефактов успешной авторизации
    def is_success_login(self):
        if self.avatar_of_user and self.name_of_user and '/login' in self.current_url:
            return True

    # Функция проверки наличия артефактов успешной выхода из под пользователя
    def is_success_logout(self):
        if not (self.avatar_of_use and self.name_of_user) and self.button_login_register:
            return True     

    # Функция клика на кнопку "Выйти"  
    def click_logout_button(self):
        self.click_element(LoginPageLocators.BUTTON_OF_LOGOUT)

    # Функция прохождения всех этапов авторизации
    def login(self, email, password):
        self.click_login_registred()
        self.enter_email_field(email)
        self.enter_password(password)
        self.click_login()

    # Функция выхода из под пользователя
    def logout(self):
        self.click_logout_button()