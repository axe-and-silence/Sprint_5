from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class Locators:

        # Кнопка "Разместить объявление" на основной странице без авторизации
        button_post_advertisement_una = By.XPATH, ".//div/div/div[1]/div/button[2]"

        # Кнопка "Разместить объявление" на основной странице с авторизацией
        #button_post_advertisement_a = By.XPATH, "/html/body/div/div/div[1]/div/button"
        button_post_advertisement_a = By.CSS_SELECTOR, ".header_shell__zlCGj > div > button"
        
        # Форма на основной странице "Чтобы разместить объявление, авторизуйтесь"
        registred_to_post_form = By.XPATH, ".//h1"

        # Текстовое поле ввода "Название" на странице "Новое объявление" 
        name_of_advertisement = By.XPATH, ".//div[1]/div/div/input"
        
        # Текстовое поле ввода "Описание товара" на странице "Новое объявление" 
        description_of_advertisement = By.XPATH , ".//div[4]/div/textarea"

        # Текстовое поле ввода "Стоимость" на странице "Новое объявление"
        cost_of_advertisement = By.XPATH, './/div[5]/div/div/input'

        # Радио кнопка "Б/У" в форме "Состояние товара" на странице "Новое объявление"
        condition_of_goods = By.XPATH, './/fieldset/div/div[2]/div'

        # Стрелка выпадающиего списке в форме "Категория" на странице "Новое объявление"
        arrow_of_category = By.XPATH,  './/div[2]/div[1]/button'

        # Категория "Хобби" в выпадающем списке "Категория" на странице "Новое объявление"
        hobby_category = By.XPATH, './/div[2]/div[2]/button[4]/span'

        # Стрелка выпадающиего списке в форме "Город" на странице "Новое объявление"
        arrow_of_city = By.XPATH, './/div[3]/div[1]/button'

        # Город "Екатеринбург" в выпадающем списке "Город" на странице "Новое объявление"
        yoburg_city = By.XPATH,'.//div[3]/div[2]/button[4]'

        # Кнопка "Опубликовать" на странице "Новое объявление"
        post_button = By.XPATH, './/form/button'

         # Кнопка "Вход и регистрация" на основной странице
        button_login_register = By.XPATH, ".//button[1]"

        # Кнопка "Нет аккаунта" на странице авторизации
        button_net_accaunta = By.CLASS_NAME, "buttonSecondary inButtonText undefined inButtonText"
        
        # Поле ввода "Введите Email" на странице авторизации
        email_field_authorization = By.NAME, 'email'

        # Поле ввода "Пароль" на странице авторизации
        password_field_authorization = By.NAME, 'password'

        # Кнопка "Войти" на странице авторизации
        button_of_login = By.XPATH, './/form/div[3]/button[1]'

         # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        avatar_of_user = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"

        # Имя пользователя на главной странице. Нужен для определения успешной авторизации
        name_of_user = By.CSS_SELECTOR, ".flexRow > div > h3" 

        # Кнопка "Выйти" на главной странице 
        button_of_logout = By.XPATH, ".//body/div/div/div[1]/div/div[1]/div/button"

        # Кнопка "Нет аккаунта" на странице авторизации
        button_net_accaunta = By.XPATH, './/form/div[3]/button[2]'

        # Поле "Введите Email" на странице регистрации
        email_field_registration = By.NAME, 'email'

        # Поле ввода "Пароль" на странице регистрации
        password_field_registration = By.NAME, 'password'

        # Поле ввода "Повторите пароль" на странице регистрации
        repeat_password_field_registration = By.NAME, 'submitPassword'

        # Кнопка "Создать аккаунт" на форме регистрации
        button_of_registration =  By.XPATH, './/form/div[3]/button[1]'

        # Красная рамка вокруг поля "Введите Email" на странице регистрации
        invalid_email_registred_email = './/div[2]/div[1]/div/div'

        # Красная рамка вокруг поля ввода "Пароль" на странице регистрации
        invalid_email_registred_password = './/div[2]/div[2]/div/div'

        # Красная рамка вокруг поля ввода "Повторите пароль" на странице регистрации
        invalid_email_registred_repeat_password = './/div[3]/div/div'

        # Красный текст "Ощибка" между полями "Введите Email" и "Пароль" на странице регистрации
        invalid_email_registred_error = './/div[1]/span'
