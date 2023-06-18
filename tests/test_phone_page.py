import pytest
from pages.phone_page import PhonePage
from pages.selected_phone_page import SelectedPhone


@pytest.mark.phones_page
def test_choose_the_purchase(driver):
    phone_page = PhonePage(driver)
    phone_page.open_phone_page()
    assert phone_page.check_that_a_necessary_page_was_opened()
    phone_page.go_to_the_purchase_of_the_selected_phone()
    selected_phone_page = SelectedPhone(driver)
    selected_phone_page.open_selected_phone_page()
    assert selected_phone_page.check_the_name_from_selected_phone

