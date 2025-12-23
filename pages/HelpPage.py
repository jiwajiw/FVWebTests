import allure
from pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class HelpPageLocators:
    SEARCH_FIELD = (By.XPATH, '//input[@type="search"]')
    ACTUAL_TODAY = (By.XPATH, '//a[contains(@href, "segodnya-aktualno")]')
    REGISTRATION = (By.XPATH, '//a[contains(@href, "registraciya")]')
    MY_PROFILE = (By.XPATH, '//a[contains(@href, "moi-profil")]')
    COMMUNICATION = (By.XPATH, '//a[contains(@href, "obshchenie")]')
    PROFILE_ACCESS = (By.XPATH, '//a[contains(@href, "dostup-k-profilu")]')
    SECURITY = (By.XPATH, '//a[contains(@href, "bezopasnost")]')
    GROUPS = (By.XPATH, '//a[contains(@href, "gruppy")]')
    PAID_FUNCTIONS = (By.XPATH, '//a[contains(@href, "platnye-funkcii")]')
    SPAM = (By.XPATH, '//a[contains(@href, "narusheniya-i-spam")]')
    GAMES_AND_APPS = (By.XPATH, '//a[contains(@href, "igry-i-prilozheniya")]')
    OTHER_SERVICES = (By.XPATH, '//a[contains(@href, "drugie-servisy")]')
    IMPORTANT_INFORMATION = (By.XPATH, '//a[contains(@href, "poleznaya-informaciya")]')
    ADVERTISEMENT_CABINET = (By.XPATH, '//a[contains(@href, "reklamnyi-kabinet")]')

class HelpPageHelper(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверить корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(HelpPageLocators.SEARCH_FIELD)
        self.find_element(HelpPageLocators.ACTUAL_TODAY)
        self.find_element(HelpPageLocators.REGISTRATION)
        self.find_element(HelpPageLocators.MY_PROFILE)
        self.find_element(HelpPageLocators.COMMUNICATION)
        self.find_element(HelpPageLocators.PROFILE_ACCESS)
        self.find_element(HelpPageLocators.SECURITY)
        self.find_element(HelpPageLocators.GROUPS)
        self.find_element(HelpPageLocators.PAID_FUNCTIONS)
        self.find_element(HelpPageLocators.GAMES_AND_APPS)
        self.find_element(HelpPageLocators.OTHER_SERVICES)
        self.find_element(HelpPageLocators.IMPORTANT_INFORMATION)
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET)

    @allure.step('Пролистать до элемента')
    def scrollToitem(self, locator):
        scroll_item = self.find_element(locator)
        ActionChains(self.driver).scroll_to_element(scroll_item).perform()

    @allure.step('Переход к рекламному кабинету')
    def click_ad_cabinet(self):
        self.attach_screenshot()
        self.find_element(HelpPageLocators.ADVERTISEMENT_CABINET).click()