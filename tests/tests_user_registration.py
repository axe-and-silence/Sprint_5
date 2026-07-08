import pytest
from pages.registration_pages import RegistrationPage
from constants import Constants
from helpers import Helpers

# Проверка регистрации нового пользователя    
def test_registration_new_user(setup_driver):  
        driver = setup_driver
        registration_page = RegistrationPage(driver)
        registration_page.registration(Helpers.new_user_email(),Constants.password)
        assert registration_page.is_success_login

# Проверка регистрации нового пользователя с невалидным мылом
def test_registration_new_user_invalid_email(setup_driver):
        driver = setup_driver
        registration_page = RegistrationPage(driver)
        registration_page.registration(Helpers.new_user_invalid_email(),Constants.password)
        assert registration_page.is_unsuccess_registration

# Проверка регистрации существующего пользователя
def test_registration_existing_user(setup_driver):
        driver = setup_driver
        registration_page = RegistrationPage(driver)
        registration_page.registration(Constants.email,Constants.password )
        assert registration_page.is_unsuccess_registration