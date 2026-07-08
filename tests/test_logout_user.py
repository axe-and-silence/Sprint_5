import pytest
from pages.login_pages import LoginPage
from constants import Constants

# Проверка авторизации существующего пользователя
def test_button_login_register(setup_driver):
        driver = setup_driver
        login_page = LoginPage(driver)
        login_page.login(Constants.email, Constants.password)
        login_page.logout
        assert login_page.is_success_login