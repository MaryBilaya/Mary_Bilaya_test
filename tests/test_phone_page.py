from pages.phone_page import PhonePage


def test(driver):
    phone_page = PhonePage(driver)
    phone_page.open_phone_page()
    phone_page.go_to_purchase()