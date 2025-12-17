import allure
from pages.BasePage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

class LoginPageLocators(BasePage):
    LOGIN_TAB = (By.XPATH, '//a[@data-l="t,login_tab"]')
    QR_TAB = (By.XPATH, '//a[@data-l="t,qr_tab"]')
    LOGIN_FIELD = (By.ID, 'field_email')
    PASSWORD_FIELD = (By.ID, 'field_password')
    LOGIN_BUTTON = (By.XPATH, '//button[.//span[text()="Войти"]]')
    QR_BUTTON = (By.XPATH, '//button[.//span[text()="Войти по QR-коду"]]')
    CAN_NOT_ENTER_BUTTON = (By.XPATH, '//button[@aria-label="Не получается войти?"]')
    REGISTRATION_BUTTON = (By.XPATH, '//button[.//span[text()="Зарегистрироваться"]]')
    RESTORE_LINK = (By.XPATH, '//a[contains(@href, "anonymRecoveryStart")]')
    VK_LINK = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAILRU_LINK = (By.XPATH, '//a[@data-l="t,mailru"]')
    GOOGLE_LINK = (By.XPATH, '//a[@data-l="t,google"]')
    YANDEX_LINK = (By.XPATH, '//a[@data-l="t,yandex"]')
    APPLE_LINK = (By.XPATH, '//a[@data-l="t,apple"]')
    ERROR_TEXT = (By.CSS_SELECTOR, "span[class*='LoginForm-module__error']")
    GO_BACK_BUTTON = (By.XPATH, '//button[.//span[text()="Отмена"]]')

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверить корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_TAB)
        self.find_element(LoginPageLocators.QR_TAB)
        self.find_element(LoginPageLocators.LOGIN_FIELD)
        self.find_element(LoginPageLocators.PASSWORD_FIELD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)
        self.find_element(LoginPageLocators.QR_BUTTON)
        self.find_element(LoginPageLocators.CAN_NOT_ENTER_BUTTON)
        self.find_element(LoginPageLocators.REGISTRATION_BUTTON)
        self.find_element(LoginPageLocators.VK_LINK)
        self.find_element(LoginPageLocators.MAILRU_LINK)
        self.find_element(LoginPageLocators.GOOGLE_LINK)
        self.find_element(LoginPageLocators.YANDEX_LINK)
        self.find_element(LoginPageLocators.APPLE_LINK)

    @allure.step('Нажать на кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получить текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Ввести логин')
    def enter_login(self, login):
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(login)
        self.attach_screenshot()

    @allure.step('Ввести пароль')
    def enter_password(self, password):
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        self.attach_screenshot()

    @allure.step('Перейти к восстановлению')
    def click_recovery(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.RESTORE_LINK).click()

    @allure.step('Очистить поле логина')
    def clear_login(self):
        self.find_element(LoginPageLocators.LOGIN_FIELD).clear()

    @allure.step('Очистить поле пароля')
    def clear_password(self):
        self.find_element(LoginPageLocators.PASSWORD_FIELD).clear()

    @allure.step('Дождаться ошибки авторизации')
    def wait_error_optional(self, time=5):
        try:
            return WebDriverWait(self.driver, time).until(
                expected_conditions.presence_of_element_located(LoginPageLocators.ERROR_TEXT)
            )
        except TimeoutException:
            return None

    @allure.step('Дождаться появления кнопки восстановления')
    def wait_recovery(self):
        return WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(LoginPageLocators.RESTORE_LINK))