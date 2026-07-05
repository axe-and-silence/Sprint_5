from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import random,string

# Фикстура на инициализацию драйвера
@pytest.fixture(scope='session')
def setup_driver():
    # Фаза настройки: инициализируем драйвер
    setup_driver = webdriver.Chrome()
    
    # Здесь мы «возвращаем» драйвер тесту — точка yield
    yield setup_driver
    
    # Фаза очистки: закрываем драйвер после теста
    setup_driver.quit()