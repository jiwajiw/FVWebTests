import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--lang=ru")
    driver = webdriver.Remote(
        command_executor="http://213.176.118.218:4444",
        options=options
    )
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()