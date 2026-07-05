from selenium.webdriver.common.by import By

class LoginPageLocators:

    # Кнопка "Вход и регистрация" на основной странице
    BUTTON_LOGIN_REGISTER = By.XPATH, ".//button[1]"

    # Кнопка "Нет аккаунта" на странице авторизации
    BUTTON_NET_ACCAUNTA = By.CLASS_NAME, "buttonSecondary inButtonText undefined inButtonText"
        
    # Поле ввода "Введите Email" на странице авторизации
    EMAIL_FIELD_AUTHORIZATION = By.NAME, 'email'

    # Поле ввода "Пароль" на странице авторизации
    PASSWORD_FIELD_AUTHORIZATION = By.NAME, 'password'

    # Кнопка "Войти" на странице авторизации
    BUTTON_OF_LOGIN = By.XPATH, './/form/div[3]/button[1]'

    # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
    AVATAR_OF_USER = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"

    # Имя пользователя на главной странице. Нужен для определения успешной авторизации
    NAME_OF_USER = By.CSS_SELECTOR, ".flexRow > div > h3" 

    # Кнопка "Выйти" на главной странице 
    BUTTON_OF_LOGOUT = By.XPATH, ".//body/div/div/div[1]/div/div[1]/div/button"