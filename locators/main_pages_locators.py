from selenium.webdriver.common.by import By

class MainPageLocators:
        # Кнопка "Разместить объявление" на основной странице без авторизации
        BUTTON_POST_ADVERTISEMENT_UNA = By.XPATH, ".//div/div/div[1]/div/button[2]"

        # Кнопка "Разместить объявление" на основной странице с авторизацией
        BUTTON_POST_ADVERTISEMENT_A = By.CSS_SELECTOR, ".header_shell__zlCGj > div > button"
        
        # Форма на основной странице "Чтобы разместить объявление, авторизуйтесь"
        REGISTRED_TO_POST_FORM = By.XPATH, ".//h1"

        # Текстовое поле ввода "Название" на странице "Новое объявление" 
        NAME_OF_ADVERTISEMENT = By.XPATH, ".//div[1]/div/div/input"
        
        # Текстовое поле ввода "Описание товара" на странице "Новое объявление" 
        DESCRIPTION_OF_ADVERTISEMENT = By.XPATH , ".//div[4]/div/textarea"

        # Текстовое поле ввода "Стоимость" на странице "Новое объявление"
        COST_OF_ADVERTISEMENT = By.XPATH, './/div[5]/div/div/input'

        # Радио кнопка "Б/У" в форме "Состояние товара" на странице "Новое объявление"
        CONDITION_OF_GOODS = By.XPATH, './/fieldset/div/div[2]/div'

        # Стрелка выпадающиего списке в форме "Категория" на странице "Новое объявление"
        ARROW_OF_CATEGORY = By.XPATH,  './/div[2]/div[1]/button'

        # Категория "Хобби" в выпадающем списке "Категория" на странице "Новое объявление"
        HOBBY_CATEGORY = By.XPATH, './/div[2]/div[2]/button[4]/span'

        # Стрелка выпадающиего списке в форме "Город" на странице "Новое объявление"
        ARROW_OF_CITY = By.XPATH, './/div[3]/div[1]/button'

        # Город "Екатеринбург" в выпадающем списке "Город" на странице "Новое объявление"
        YOBURG_CITY = By.XPATH,'.//div[3]/div[2]/button[4]'

        # Кнопка "Опубликовать" на странице "Новое объявление"
        POST_BUTTON = By.XPATH, './/form/button'

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        AVATAR_OF_USER = By.CSS_SELECTOR, ".header_shell__zlCGj > div > div.flexRow > button > svg"