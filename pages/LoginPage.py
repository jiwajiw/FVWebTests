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

class LoginPageHelper(BasePage):
    pass