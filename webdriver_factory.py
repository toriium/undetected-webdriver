from abc import ABC, abstractmethod
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as OptionsChorme
from selenium.webdriver.firefox.options import Options as OptionsFirefox


class WebDriverABC(ABC):
    @staticmethod
    @abstractmethod
    def create_driver(): pass


class ChomeWebDriver(WebDriverABC):
    @staticmethod
    def create_driver():
        options = OptionsChorme()
        options.add_argument('--incognito')
        driver = Chrome(options=options)
        return driver


class FirefoxWebDriver(WebDriverABC):
    @staticmethod
    def create_driver():
        ...


class DriverFactory:
    @staticmethod
    def get_driver():
        driver = ChomeWebDriver.create_driver()
        return driver
