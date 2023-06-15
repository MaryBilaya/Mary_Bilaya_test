from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

btn_go_to_purchase = (By.CSS_SELECTOR, 'a[id="product-tile-button_3"]')


class PhonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # открыть браузер на странице главная/интернет-магазин/телефоны
    def open_phone_page(self):
        self.driver.get(self.base_url)

    # нажать кнопку "Перейти к покупке" Apple iPhone 13 128GB темная ночь [A2633]
    def go_to_purchase(self):
        btn = self.find_element(btn_go_to_purchase)
        self.driver.execute_script("arguments[0].click();", btn)





