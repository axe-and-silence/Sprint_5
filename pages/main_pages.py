from selenium.webdriver.remote.webdriver import WebDriver
from .base_page import BasePage
from locators.login_pages_locators import LoginPageLocators
from locators.main_pages_locators import MainPageLocators
from pages.login_pages import LoginPage

class MainPage(BasePage):
    
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.go_to_page()
 
    # Функция клика на кнопке "Разместить объявление" без авторизации
    def click_post_button_una(self):
        self.click_element(MainPageLocators.BUTTON_POST_ADVERTISEMENT_UNA)    

    # Функция клика на кнопке "Разместить объявление" пользователем с авторизацией   
    def click_post_button_a(self):
        try:
            self.click_element(MainPageLocators.BUTTON_POST_ADVERTISEMENT_A)
        except:
    # Повторяем поиск при возникновении ошибки
            self.click_element(MainPageLocators.BUTTON_POST_ADVERTISEMENT_A)  
                   

    # Функция проверки появления формы "Чтобы разместить объявление, авторизуйтесь"
    def check_login_for_post_form(self):
        if self.registred_to_post_form:
            return True
        
    # Функция ввода названия в поле "Название" на странице "Новое объявление"
    def enter_name_advertisement(self, name):
        self.enter_text(MainPageLocators.NAME_OF_ADVERTISEMENT, name)

    # Функция ввода описания в поле "Описание товара" на странице "Новое объявление"
    def enter_description_advertisement(self, description):
        self.enter_text(MainPageLocators.DESCRIPTION_OF_ADVERTISEMENT, description)

    # Функция ввода стоимости в поле "Стоимость" на странице "Новое объявление"
    def enter_cost_advertisement(self, cost):
        self.enter_text(MainPageLocators.COST_OF_ADVERTISEMENT, cost)  

    # Функция клика по радио кнопке "Б/У" в форме "Состояние товара" на странице "Новое объявление"   
    def click_bu_condition(self):
        self.click_element(MainPageLocators.CONDITION_OF_GOODS)

    # Функция клика по стрелке выпадающего списка "Категория товара" на странице "Новое объявление"   
    def click_arrow_of_category(self):
        self.click_element(MainPageLocators.ARROW_OF_CATEGORY)
    
    # Функция клика по "Хобби" в выпадающем списке "Категория товара" на странице "Новое объявление"   
    def click_hobby_category(self):
        self.click_element(MainPageLocators.HOBBY_CATEGORY) 
    
    # Функция клика по стрелке выпадающего списка "Город" на странице "Новое объявление" 
    def click_arrow_of_city(self):
        self.click_element(MainPageLocators.ARROW_OF_CITY) 

    # Функция клика по "Екатеринбург" в выпадающем списке "Город" на странице "Новое объявление"   
    def click_yoburg_city(self):
        self.click_element(MainPageLocators.YOBURG_CITY) 

    # Функция клика на кнопке "Разместить объявление" на странице "Новое объявление"   
    def click_post_button(self):
        self.click_element(MainPageLocators.POST_BUTTON) 

    # Функция клика аватарке на главной странице    
    def click_avatar_of_user(self):
        self.click_element(LoginPageLocators.AVATAR_OF_USER) 
    
    # Функция проверки наличия объявления
    def check_of_advertisement(self):
        self.click_avatar_of_user()
        if self.find_element_by_alt('Мопед'):
            return True
    

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

    # Функция размещения объявления авторизованного пользователя
    def post_advertisement(self,email,password,name,description,cost):
    
        self.click_login_registred()
        self.enter_email_field(email)
        self.enter_password(password)
        self.click_login()
        self.click_post_button_a()
        self.enter_name_advertisement(name)
        self.enter_description_advertisement(description)
        self.enter_cost_advertisement(cost)
        self.click_bu_condition()
        self.click_arrow_of_category()
        self.click_hobby_category()
        self.click_arrow_of_city()
        self.click_yoburg_city()
        self.click_post_button()
