from webdriver_factory import DriverFactory

driver = DriverFactory.get_driver(browser_chosen='chrome')

driver.get('https://www.google.com/')

driver.close()

