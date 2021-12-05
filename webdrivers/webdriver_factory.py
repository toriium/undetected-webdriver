import os
from abc import ABC, abstractmethod

from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options as OptionsOpera
from selenium.webdriver.chrome.options import Options as OptionsChorme
from selenium.webdriver.firefox.options import Options as OptionsFirefox

WEBDRIVERS_PATH = os.path.dirname(os.path.realpath(__file__))


class WebDriverABC(ABC):
    @classmethod
    @abstractmethod
    def create_driver(cls): pass

    @staticmethod
    @abstractmethod
    def __get_driver_options(): pass


class OperaWebDriver(WebDriverABC):
    @classmethod
    def create_driver(cls):
        options = cls.__get_driver_options()
        webdriver_path = f'{WEBDRIVERS_PATH}\\operadriver'
        driver = Opera(executable_path=webdriver_path, options=options)
        return driver

    @staticmethod
    def __get_driver_options():
        options = OptionsOpera()
        options.binary_location = r'C:\Users\user\AppData\Local\Programs\Opera GX\opera.exe'
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


class ChomeWebDriver(WebDriverABC):
    @classmethod
    def create_driver(cls):
        options = cls.__get_driver_options()
        webdriver_path = f'{WEBDRIVERS_PATH}\\chromedriver'
        driver = Chrome(executable_path=webdriver_path, options=options)
        return driver

    @staticmethod
    def __get_driver_options():
        options = OptionsChorme()
        options.binary_location = r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
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
        options = cls.__get_driver_options()
        webdriver_path = f'{WEBDRIVERS_PATH}\\geckodriver'
        driver = Firefox(executable_path=webdriver_path, options=options)
        return driver

    @staticmethod
    def __get_driver_options():
        options = OptionsFirefox()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        # options.add_argument('--headless')
        options.add_argument('--incognito')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--enable-automation')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-gpu')
        options.add_argument(
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
        return options


class DriverFactory:
    __driver = None

    @classmethod
    def get_driver(cls, chosen_browser):
        if chosen_browser == 'chrome':
            cls.__driver = ChomeWebDriver.create_driver()
        elif chosen_browser == 'firefox':
            cls.__driver = FirefoxWebDriver.create_driver()
        elif chosen_browser == 'opera':
            cls.__driver = OperaWebDriver.create_driver()
        else:
            raise ValueError(f'"{chosen_browser}" is not a valid browser, please choice a valid browser.')

        cls.__execute_scripts_in_driver(chosen_browser=chosen_browser)

        return cls.__driver

    @classmethod
    def __execute_scripts_in_driver(cls, chosen_browser):
        # execute scripts in browser to not be detected as bot
        cls.__driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        if chosen_browser != 'firefox':
            cls.__driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source":
                    "const newProto = navigator.__proto__;"
                    "delete newProto.webdriver;"
                    "navigator.__proto__ = newProto;"
            })
