from webdriver_factory import DriverFactory

driver = DriverFactory.get_driver(chosen_browser='chrome')
# driver = DriverFactory.get_driver(chosen_browser='firefox')

driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
})

driver.get('https://bot.incolumitas.com/')
driver.close()

