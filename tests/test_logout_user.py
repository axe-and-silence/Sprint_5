from selenium import webdriver
from pages.login_pages import LoginPage
import pytest

# Проверка выхода из под пользователя    
def test_button_logout(get_driver,site,user):
        get_driver.get(site)
        login_page = LoginPage(get_driver)
        login_page.login(user.email, user.password)
        login_page.logout()
        assert login_page.is_success_logout 
        get_driver.quit()