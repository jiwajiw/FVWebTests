import allure
from pages.BasePage import BasePage
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
    VK_LINK = (By.XPATH, '//a[@data-l="t,vkc"]')
    MAILRU_LINK = (By.XPATH, '//a[@data-l="t,mailru"]')
    GOOGLE_LINK = (By.XPATH, '//a[@data-l="t,google"]')
    YANDEX_LINK = (By.XPATH, '//a[@data-l="t,yandex"]')
    APPLE_LINK = (By.XPATH, '//a[@data-l="t,apple"]')
    ERROR_TEXT = (By.CSS_SELECTOR, "span[class*='LoginForm-module__error']")

class LoginPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
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

    @allure.step('Нажать на кнпоку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Получать текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginPageLocators.ERROR_TEXT).text

    @allure.step('Ввести логин')
    def enter_login(self, login):
        login_field = self.find_element(LoginPageLocators.LOGIN_FIELD)
        login_field.send_keys(login)

    @allure.step('Ввести пароль')
    def enter_password_field(self, password):
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)