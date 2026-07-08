from selenium.webdriver.common.by import By

class RegistrationPageLocators:

        # Кнопка "Вход и регистрация" на основной странице
        BUTTON_LOGIN_REGISTER = By.XPATH, "//button[@type='button' and normalize-space()='Вход и регистрация']"

        # Кнопка "Нет аккаунта" на странице авторизации
        BUTTON_NET_ACCAUNTA = By.XPATH, "//button[@type='button' and normalize-space()='Нет аккаунта']"
   
        # Поле "Введите Email" на странице регистрации
        EMAIL_FIELD_REGISTRATION = By.NAME, 'email'

        # Поле ввода "Пароль" на странице регистрации
        PASSWORD_FIELD_REGISTRATION = By.NAME, 'password'

        # Поле ввода "Повторите пароль" на странице регистрации
        REPEAT_PASSWORD_FIELD_REGISTRATION = By.NAME, 'submitPassword'

        # Кнопка "Создать аккаунт" на форме регистрации
        BUTTON_OF_REGISTRATION =  By.XPATH, "//button[@type='submit' and normalize-space()='Создать аккаунт']"

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        AVATAR_OF_USER = By.CSS_SELECTOR, "button[data-testid='btn-logout']"

        # Имя пользователя на главной странице. Нужен для определения успешной авторизации
        NAME_OF_USER = By.XPATH, "//h3[normalize-space()='User.']" 

        # Красная рамка вокруг поля "Введите Email" на странице регистрации
        INVALID_EMAIL_REGISTRED_EMAIL = By.XPATH, "//input[@name='email']/parent::div[contains(@class, 'input_inputError')]"

        # Красная рамка вокруг поля ввода "Пароль" на странице регистрации
        INVALID_EMAIL_REGISTRED_PASSWORD = By.XPATH, "//input[@name='password']/parent::div[contains(@class, 'input_inputError')]"

        # Красная рамка вокруг поля ввода "Повторите пароль" на странице регистрации
        INVALID_EMAIL_REGISTRED_REPEAT_PASSWOR = By.XPATH, "//input[@name='submitPassword']/parent::div[contains(@class, 'input_inputError')]"

        # Красный текст "Ошибка" между полями "Введите Email" и "Пароль" на странице регистрации
        INVALID_EMAIL_REGISTRED_ERROR = By.XPATH, "//span[normalize-space()='Ошибка']"