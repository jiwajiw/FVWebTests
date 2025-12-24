import allure
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By
#CAN BE WRONG, RECHECK
class VKEcosystemLocators:
    TITLE_LABEL = (By.XPATH, '//h1[@class="title-h2"]')

class VKEcosystemPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверить корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(VKEcosystemLocators.TITLE_LABEL)