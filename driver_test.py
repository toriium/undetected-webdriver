from webdriver_factory import DriverFactory

# driver = DriverFactory.get_driver(chosen_browser='chrome')
driver = DriverFactory.get_driver(chosen_browser='firefox')

driver.get('https://www.google.com/')
driver.close()

