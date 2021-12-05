import time

from webdrivers.webdriver_factory import DriverFactory

# driver = DriverFactory.get_driver(chosen_browser='opera')
# driver = DriverFactory.get_driver(chosen_browser='firefox')
driver = DriverFactory.get_driver(chosen_browser='chrome')

driver.get('https://bot.incolumitas.com/')
time.sleep(10)
driver.close()

