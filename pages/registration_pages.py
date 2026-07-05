from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from locators.registration_pages_locators import RegistrationPageLocators
from locators.login_pages_locators import LoginPageLocators

class RegistrationPage(BasePage):
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.go_to_page()

    # Функция клика на кнопке "Вход и регистрация"        
    def click_login_registred(self):
        self.click_element(LoginPageLocators.BUTTON_LOGIN_REGISTER)
    
    # Функция клика на кнопку "Нет аккаунта"    
    def click_button_net_accaunta(self):
        self.click_element(RegistrationPageLocators.BUTTON_NET_ACCAUNTA)
    
    # Функция ввода email на странице регистрации
    def enter_email_field_registration(self, email):
        self.enter_text(RegistrationPageLocators.EMAIL_FIELD_REGISTRATION, email)
    
    # Функция ввода валидного пароля
    def enter_password_registration(self, password):
        self.enter_text(RegistrationPageLocators.PASSWORD_FIELD_REGISTRATION, password)
    
    # Функция ввода повтора пороля
    def enter_password_registration_repeat(self, password):
        self.enter_text(RegistrationPageLocators.REPEAT_PASSWORD_FIELD_REGISTRATION, password)

    # Функция клика на кнопку "Создать аккаунт"    
    def click_button_of_registration(self):
        self.click_element(RegistrationPageLocators.BUTTON_OF_REGISTRATION)
    
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