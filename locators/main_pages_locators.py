from selenium.webdriver.common.by import By

class MainPageLocators:
        # Кнопка "Разместить объявление" на основной странице без авторизации
        BUTTON_POST_ADVERTISEMENT_UNA = By.XPATH, "//button[@type='button' and normalize-space()='Разместить объявление']"
        
        # Кнопка "Разместить объявление" на основной странице с авторизацией
        BUTTON_POST_ADVERTISEMENT_A = By.XPATH, "//button[contains(., 'Разместить объявление')]"

        # Форма на основной странице "Чтобы разместить объявление, авторизуйтесь"
        REGISTRED_TO_POST_FORM = By.XPATH, "//h1[normalize-space()='Чтобы разместить объявление, авторизуйтесь']"

        # Текстовое поле ввода "Название" на странице "Новое объявление" 
        NAME_OF_ADVERTISEMENT = By.CSS_SELECTOR, "input[name='name']"
        
        # Текстовое поле ввода "Описание товара" на странице "Новое объявление" 
        DESCRIPTION_OF_ADVERTISEMENT = By.CSS_SELECTOR, "textarea[name='description']"

        # Текстовое поле ввода "Стоимость" на странице "Новое объявление"
        COST_OF_ADVERTISEMENT = By.CSS_SELECTOR, "input[name='price']"

        # Радио кнопка "Б/У" в форме "Состояние товара" на странице "Новое объявление"
        CONDITION_OF_GOODS = By.CSS_SELECTOR, "div.radioUnput_inputRegular__FbVbr"
        # By.XPATH, ".//fieldset/div/div[2]/div"

        # Стрелка выпадающиего списке в форме "Категория" на странице "Новое объявление"
        ARROW_OF_CATEGORY = By.CSS_SELECTOR, "button[type='button'][class*='dropDownMenu']"

        # Категория "Хобби" в выпадающем списке "Категория" на странице "Новое объявление"
        HOBBY_CATEGORY = By.XPATH, "//span[normalize-space()='Хобби']"

        # Стрелка выпадающиего списке в форме "Город" на странице "Новое объявление"
        ARROW_OF_CITY = (
    By.XPATH,
    "//input[@name='city']/following::button[contains(@class,'dropDownMenu_arrowDown__pfGL1')][1]//*[name()='svg' and @width='7' and @height='12']"
)
        # Город "Екатеринбург" в выпадающем списке "Город" на странице "Новое объявление"
        YOBURG_CITY = By.XPATH, "//button[@type='button' and normalize-space()='Екатеринбург']"

        # Кнопка "Опубликовать" на странице "Новое объявление"
        POST_BUTTON = By.XPATH, "//button[@type='submit' and normalize-space()='Опубликовать']"

        # Аватарка пользователя на главной странице. Нужна для определения успешной авторизации
        AVATAR_OF_USER = By.CSS_SELECTOR, "button[data-testid='btn-logout']"