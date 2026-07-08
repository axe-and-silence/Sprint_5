from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
    
    def go_to_page(self):
        self.driver.get(Constants.base_url)
    
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
    
    def click_element(self, locator, timeout=10):
                return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable (locator)
        ).click()
  
    def enter_text(self, locator, text, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)