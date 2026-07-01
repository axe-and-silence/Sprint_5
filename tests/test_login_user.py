from selenium import webdriver
from pages.login_pages import LoginPage
import pytest

# Проверка авторизации существующего пользователя
def test_button_login_register(get_driver,site,user):
        get_driver.get(site)
        login_page = LoginPage(get_driver)
        login_page.login(user.email, user.password)
        assert login_page.is_success_login 
        get_driver.quit()