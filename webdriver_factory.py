from abc import ABC, abstractmethod
from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium.webdriver.chrome.options import Options as OptionsChorme
from selenium.webdriver.firefox.options import Options as OptionsFirefox


class WebDriverABC(ABC):
    @abstractmethod
    def __call__(self, *args, **kwargs): pass


class ChomeWebDriver(WebDriverABC):
    def __call__(self, *args, **kwargs):
        ...


class FirefoxWebDriver(WebDriverABC):
    def __call__(self, *args, **kwargs):
        ...


class DriverFactory:
    def __call__(self, *args, **kwargs):
        ...
