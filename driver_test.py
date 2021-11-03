from webdriver_factory import DriverFactory

options = {
    'incognito': True
}
driver = DriverFactory.get_driver(chosen_browser='chrome', driver_options=options)

driver.get('https://www.google.com/')

driver.close()

