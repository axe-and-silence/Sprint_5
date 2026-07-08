import pytest
from pages.login_pages import LoginPage
from pages.main_pages import MainPage
from constants import Constants


# Проверка формы "Чтобы разместить объявление, авторизуйтесь"   
def test_post_need_login_form(setup_driver):
        driver = setup_driver
        main_page = MainPage(driver)
        main_page.click_post_button_una()
        assert main_page.check_login_for_post_form

# Проверка размещения нового объявления. Предварительно использует готовый процесс авторизации
def test_post_advertisement(setup_driver):
        driver = setup_driver
        main_pages = MainPage(driver)
        main_pages.post_advertisement(Constants.email, Constants.password,Constants.advertisement_name,Constants.advertisement_description,Constants.advertisement_cost)
        assert main_pages.check_of_advertisement