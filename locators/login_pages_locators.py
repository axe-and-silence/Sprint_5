from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Кнопка "Вход и регистрация" на основной странице
    BUTTON_LOGIN_REGISTER = By.XPATH, "//button[@type='button' and normalize-space()='Вход и регистрация']"

    # Кнопка "Нет аккаунта" на странице авторизации
    BUTTON_NET_ACCAUNTA = By.XPATH, "//button[@type='button' and normalize-space()='Нет аккаунта']"
        
    # Поле ввода "Введите Email" на странице авторизации
    EMAIL_FIELD_AUTHORIZATION = By.CSS_SELECTOR, "input[name='email']"

    # Поле ввода "Пароль" на странице авторизации
    PASSWORD_FIELD_AUTHORIZATION = By.CSS_SELECTOR, "input[name='password']"

    # Кнопка "Войти" на странице авторизации
    BUTTON_OF_LOGIN = By.XPATH, "//button[@type='submit' and normalize-space()='Войти']"

    # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
    AVATAR_OF_USER = By.CSS_SELECTOR, "button[data-testid='btn-logout']"

    # Имя пользователя на главной странице. Нужен для определения успешной авторизации
    NAME_OF_USER = By.XPATH, "//h3[normalize-space()='User.']" 

    # Кнопка "Выйти" на главной странице 
    BUTTON_OF_LOGOUT = By.XPATH, "//button[@type='button' and normalize-space()='Выйти']"