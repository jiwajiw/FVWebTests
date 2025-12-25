import allure
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.RecoveryPage import RecoveryPageHelper

BASE_URL = 'https://ok.ru/'
LOGIN_TEXT = "test@gmail.com"
PASSWORD_TEXT = "111111"

@allure.suite('Проверка восстановления пользователя')
@allure.title('Проверка перехода к восстановлению после нескольких неудачных попыток авторизации')
def test_go_to_recovery_after_fails(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    for i in range(3):
        LoginPage.clear_login()
        LoginPage.clear_password()
        LoginPage.enter_login(LOGIN_TEXT)
        LoginPage.enter_password(PASSWORD_TEXT)
        LoginPage.click_login()
        LoginPage.wait_error_optional()
    LoginPage.wait_recovery()
    LoginPage.click_recovery()
    RecoveryPageHelper(browser)