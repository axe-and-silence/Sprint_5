from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import pytest
from pages.main_pages import MainPage
from pages.login_pages import LoginPage

# Проверка формы "Чтобы разместить объявление, авторизуйтесь"   
def test_post_need_login_form(get_driver,site):
        get_driver.get(site)
        main_page = MainPage(get_driver)
        main_page.click_post_button_una()
        assert main_page.check_login_for_post_form
        get_driver.quit()

# Проверка размещения нового объявления. Предварительно использует готовый процесс авторизации
def test_post_advertisement(get_driver,site,advertisement,user):
        get_driver.get(site)
        login_page = LoginPage(get_driver)
        login_page.login(user.email, user.password)
        main_pages = MainPage(get_driver)
        main_pages.post_advertisement(advertisement.name,advertisement.description,advertisement.cost)
        assert main_pages.check_of_advertisement
        get_driver.quit()