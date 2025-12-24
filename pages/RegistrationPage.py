import allure
import random
from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    PHONE_FIELD = (By.CSS_SELECTOR, "input.js-phone")
    COUNTRY_LIST = (By.CSS_SELECTOR, "div.country-select_label input.js-country-input")
    COUNTRY_ITEM = (By.CSS_SELECTOR, "div.country-select_code")
    SUBMIT_BUTTON = (By.XPATH, '//input[@data-l="t,submit"]')
    SUPPORT_BUTTON = (By.CSS_SELECTOR, 'a.ext-registration_f-support-link')

class RegistrationPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверить корректность загрузки страницы'):
            self.find_elements(RegistrationPageLocators.PHONE_FIELD)
            self.find_elements(RegistrationPageLocators.COUNTRY_LIST)
            self.find_elements(RegistrationPageLocators.SUBMIT_BUTTON)
            self.find_elements(RegistrationPageLocators.SUPPORT_BUTTON)

    @allure.step('Выбрать случайный номер страны')
    def select_random_country(self):
        random_number = random.randint(1, 212)
        self.find_element(RegistrationPageLocators.COUNTRY_LIST, random_number).click()
        country_items = self.find_elements(RegistrationPageLocators.COUNTRY_ITEM)
        country_code = country_items[random_number].text
        country_items[random_number].click()
        return country_code

    @allure.step('Получить значение кода страны')
    def get_country_phone_value(self):
        return self.find_element(RegistrationPageLocators.PHONE_FIELD).get_attribute('value')