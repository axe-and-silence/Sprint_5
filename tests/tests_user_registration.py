from selenium import webdriver
from pages.registration_pages import RegistrationPage
import pytest

# Проверка регистрации нового пользователя    
def test_registration_new_user(get_driver,site,new_user_password,new_user_email):  
        get_driver.get(site)
        registration_page = RegistrationPage(get_driver)
        registration_page.registration(new_user_email, new_user_password)
        assert registration_page.is_success_login
        get_driver.quit()

# Проверка регистрации нового пользователя с невалидным мылом
def test_registration_new_user_invalid_email(get_driver,site,new_user_password,new_user_invalid_email):
        get_driver.get(site)
        registration_page = RegistrationPage(get_driver)
        registration_page.registration(new_user_invalid_email, new_user_password)
        assert registration_page.is_unsuccess_registration
        get_driver.quit()

# Проверка регистрации существующего пользователя
def test_registration_existing_user(get_driver,site,user):
        get_driver.get(site)
        registration_page = RegistrationPage(get_driver)
        registration_page.registration(user.email, user.password)
        assert registration_page.is_unsuccess_registration
        get_driver.quit()