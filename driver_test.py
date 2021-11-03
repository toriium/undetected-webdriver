from webdriver_factory import DriverFactory

driver = DriverFactory.get_driver()

driver.get('https://www.google.com/')

driver.close()

