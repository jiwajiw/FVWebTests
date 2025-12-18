import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RecoveryPageLocators:
    PHONE_BUTTON = (By.XPATH, '//a[@data-l="t,phone"]')
    EMAIL_BUTTON = (By.XPATH, '//a[@data-l="t,email"]')
    QR_CODE = (By.XPATH, '//img[contains(@class,"qr_code_image")]')
    SUPPORT_BUTTON = (By.CSS_SELECTOR, 'a.ext-registration_f-support-link')

class RecoveryPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверить корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(RecoveryPageLocators.PHONE_BUTTON)
        self.find_element(RecoveryPageLocators.EMAIL_BUTTON)
        self.find_element(RecoveryPageLocators.QR_CODE)
        self.find_element(RecoveryPageLocators.SUPPORT_BUTTON)