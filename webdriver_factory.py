from abc import ABC, abstractmethod
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as OptionsChorme
from selenium.webdriver.firefox.options import Options as OptionsFirefox


class WebDriverABC(ABC):
    @classmethod
    @abstractmethod
    def create_driver(cls): pass

    @classmethod
    @abstractmethod
    def get_driver_options(cls): pass


class ChomeWebDriver(WebDriverABC):
    @classmethod
    def create_driver(cls):
        options = cls.get_driver_options()
        driver = Chrome(options=options)
        return driver

    @classmethod
    def get_driver_options(cls):
        options = OptionsChorme()
        options.add_argument('--incognito')
        return options


class FirefoxWebDriver(WebDriverABC):
    @classmethod
    def create_driver(cls):
        options = cls.get_driver_options()
        driver = Firefox(options=options)
        return driver

    @classmethod
    def get_driver_options(cls):
        options = OptionsFirefox()
        options.add_argument('--incognito')
        return options


class DriverFactory:
    @staticmethod
    def get_driver(chosen_browser):
        if chosen_browser == 'chrome':
            return ChomeWebDriver.create_driver()

        if chosen_browser == 'firefox':
            return FirefoxWebDriver.create_driver()
