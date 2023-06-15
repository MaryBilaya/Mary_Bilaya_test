from selenium.webdriver.chrome.webdriver import WebDriver

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.base_url = 'https://www.a1.by/ru/shop/c/phones'

    def find_element(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_element(by_name, by_value)

    def find_elements(self, args: tuple):
        by_name, by_value = args
        return self.driver.find_elements(by_name, by_value)





