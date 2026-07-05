from selenium.webdriver.common.by import By

class RegistrationPageLocators:

        # Кнопка "Вход и регистрация" на основной странице
        BUTTON_LOGIN_REGISTER = By.XPATH, ".//button[1]"

        # Кнопка "Нет аккаунта" на странице авторизации
        BUTTON_NET_ACCAUNTA = By.XPATH, './/form/div[3]/button[2]'

        # Поле "Введите Email" на странице регистрации
        EMAIL_FIELD_REGISTRATION = By.NAME, 'email'

        # Поле ввода "Пароль" на странице регистрации
        PASSWORD_FIELD_REGISTRATION = By.NAME, 'password'

        # Поле ввода "Повторите пароль" на странице регистрации
        REPEAT_PASSWORD_FIELD_REGISTRATION = By.NAME, 'submitPassword'

        # Кнопка "Создать аккаунт" на форме регистрации
        BUTTON_OF_REGISTRATION =  By.XPATH, './/form/div[3]/button[1]'

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        AVATAR_OF_USE = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"

        # Имя пользователя на главной странице. Нужен для определения успешной авторизации
        NAME_OF_USER = By.CSS_SELECTOR, ".flexRow > div > h3"  

        # Красная рамка вокруг поля "Введите Email" на странице регистрации
        INVALID_EMAIL_REGISTRED_EMAIL = './/div[2]/div[1]/div/div'

        # Красная рамка вокруг поля ввода "Пароль" на странице регистрации
        INVALID_EMAIL_REGISTRED_PASSWORD = './/div[2]/div[2]/div/div'

        # Красная рамка вокруг поля ввода "Повторите пароль" на странице регистрации
        INVALID_EMAIL_REGISTRED_REPEAT_PASSWOR = './/div[3]/div/div'

        # Красный текст "Ощибка" между полями "Введите Email" и "Пароль" на странице регистрации
        INVALID_EMAIL_REGISTRED_ERROR = './/div[1]/span'