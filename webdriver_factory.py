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
        # options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--enable-automation')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
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
        # options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--enable-automation')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
        return options


class DriverFactory:
    @staticmethod
    def get_driver(chosen_browser):
        if chosen_browser == 'chrome':
            return ChomeWebDriver.create_driver()

        if chosen_browser == 'firefox':
            return FirefoxWebDriver.create_driver()
