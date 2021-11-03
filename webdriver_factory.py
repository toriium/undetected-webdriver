from abc import ABC, abstractmethod
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as OptionsChorme
from selenium.webdriver.firefox.options import Options as OptionsFirefox


class WebDriverABC(ABC):
    @classmethod
    @abstractmethod
    def create_driver(cls, driver_options: dict): pass

    @classmethod
    @abstractmethod
    def __get_driver_options(cls, driver_options: dict): pass


class ChomeWebDriver(WebDriverABC):
    @classmethod
    def create_driver(cls, driver_options: dict):
        options = cls.__get_driver_options(driver_options)
        driver = Chrome(options=options)
        return driver

    @classmethod
    def __get_driver_options(cls, driver_options):
        options = OptionsChorme()
        if driver_options['incognito']:
            options.add_argument('--incognito')
        return options


class FirefoxWebDriver(WebDriverABC):
    @classmethod
    def create_driver(cls, driver_options: dict): pass

    @classmethod
    def __get_driver_options(cls, driver_options: dict): pass


class DriverFactory:
    @staticmethod
    def get_driver(chosen_browser: str, driver_options: dict):
        if chosen_browser == 'chrome':
            return ChomeWebDriver.create_driver(driver_options)

        if chosen_browser == 'firefox':
            return FirefoxWebDriver.create_driver(driver_options)
