from selenium.webdriver.common.by import By
import selenium
from selenium.webdriver.remote.webdriver import WebDriver
import pytest


class MainPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

        # Кнопка "Разместить объявление" на основной странице без авторизации
        self.button_post_advertisement_una = By.XPATH, ".//div/div/div[1]/div/button[2]"

        # Кнопка "Разместить объявление" на основной странице с авторизацией
        #self.button_post_advertisement_a = By.XPATH, "/html/body/div/div/div[1]/div/button"
        self.button_post_advertisement_a = By.CSS_SELECTOR, ".header_shell__zlCGj > div > button"
        
        # Форма на основной странице "Чтобы разместить объявление, авторизуйтесь"
        self.registred_to_post_form = By.XPATH, ".//h1"

        # Текстовое поле ввода "Название" на странице "Новое объявление" 
        self.name_of_advertisement = By.XPATH, ".//div[1]/div/div/input"
        
        # Текстовое поле ввода "Описание товара" на странице "Новое объявление" 
        self.description_of_advertisement = By.XPATH , ".//div[4]/div/textarea"

        # Текстовое поле ввода "Стоимость" на странице "Новое объявление"
        self.cost_of_advertisement = By.XPATH, './/div[5]/div/div/input'

        # Радио кнопка "Б/У" в форме "Состояние товара" на странице "Новое объявление"
        self.condition_of_goods = By.XPATH, './/fieldset/div/div[2]/div'

        # Стрелка выпадающиего списке в форме "Категория" на странице "Новое объявление"
        self.arrow_of_category = By.XPATH,  './/div[2]/div[1]/button'

        # Категория "Хобби" в выпадающем списке "Категория" на странице "Новое объявление"
        self.hobby_category = By.XPATH, './/div[2]/div[2]/button[4]/span'

        # Стрелка выпадающиего списке в форме "Город" на странице "Новое объявление"
        self.arrow_of_city = By.XPATH, './/div[3]/div[1]/button'

        # Город "Екатеринбург" в выпадающем списке "Город" на странице "Новое объявление"
        self.yoburg_city = By.XPATH,'.//div[3]/div[2]/button[4]'

        # Кнопка "Опубликовать" на странице "Новое объявление"
        self.post_button = By.XPATH, './/form/button'

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        self.avatar_of_user = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"


    # Функция клика на кнопке "Разместить объявление" без авторизации    
    def click_post_button_una(self):
        post_button_button_una = self.driver.find_element(*self.button_post_advertisement_una)
        post_button_button_una.click()
    
    # Функция клика на кнопке "Разместить объявление" пользователем с авторизацией   
    def click_post_button_a(self):
        try:
            self.driver.find_element(*self.button_post_advertisement_a).click()
        except:
    # Повторяем поиск при возникновении ошибки
            self.driver.find_element(*self.button_post_advertisement_a).click()       



    # Функция проверки появления формы "Чтобы разместить объявление, авторизуйтесь"
    def check_login_for_post_form(self):
        if self.registred_to_post_form:
            return True
        
    # Функция ввода названия в поле "Название" на странице "Новое объявление"
    def enter_name_advertisement(self, name):
        name_advertisement_field = self.driver.find_element(*self.name_of_advertisement)
        name_advertisement_field.send_keys(name)

    # Функция ввода описания в поле "Описание товара" на странице "Новое объявление"
    def enter_description_advertisement(self, description):
        description_advertisement_field = self.driver.find_element(*self.description_of_advertisement)
        description_advertisement_field.send_keys(description)

    # Функция ввода стоимости в поле "Стоимость" на странице "Новое объявление"
    def enter_cost_advertisement(self, cost):
        cost_advertisement_field = self.driver.find_element(*self.cost_of_advertisement)
        cost_advertisement_field.send_keys(cost)   

    # Функция клика по радио кнопке "Б/У" в форме "Состояние товара" на странице "Новое объявление"   
    def click_bu_condition(self):
        bu_condition_button = self.driver.find_element(*self.condition_of_goods)
        bu_condition_button.click()

    # Функция клика по стрелке выпадающего списка "Категория товара" на странице "Новое объявление"   
    def click_arrow_of_category(self):
        arrow_of_category = self.driver.find_element(*self.arrow_of_category)
        arrow_of_category.click()
    
    # Функция клика по "Хобби" в выпадающем списке "Категория товара" на странице "Новое объявление"   
    def click_hobby_category(self):
        hobby_category = self.driver.find_element(*self.hobby_category)
        hobby_category.click() 
    
    # Функция клика по стрелке выпадающего списка "Город" на странице "Новое объявление" 
    def click_arrow_of_city(self):
        arrow_of_city = self.driver.find_element(*self.arrow_of_city)
        arrow_of_city.click()

    # Функция клика по "Екатеринбург" в выпадающем списке "Город" на странице "Новое объявление"   
    def click_yoburg_city(self):
        yoburg_city = self.driver.find_element(*self.yoburg_city)
        yoburg_city.click()

    # Функция клика на кнопке "Разместить объявление" на странице "Новое объявление"   
    def click_post_button(self):
        post_button_button = self.driver.find_element(*self.post_button)
        post_button_button.click()

    # Функция клика аватарке на главной странице    
    def click_avatar_of_user(self):
        avatar_of_user = self.driver.find_element(*self.avatar_of_user)
        avatar_of_user.click()
    
    # Функция проверки наличия объявления
    def check_of_advertisement(self):
        self.click_avatar_of_user()
        if self.driver.find_element_by_alt('Мопед'):
            return True
    
    # Функция размещения объявления авторизованного пользователя
    def post_advertisement(self,name,description,cost):
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
