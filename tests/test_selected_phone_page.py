from pages.selected_phone_page import SelectedPhone
from pages.sign_in_page import SignInPage
import pytest


@pytest.mark.selected_phone_page
def test_way_of_payment(driver):
    selected_phone_page = SelectedPhone(driver)
    selected_phone_page.open_selected_phone_page()
    assert selected_phone_page.check_that_page_of_selected_phone_was_opened()
    selected_phone_page.choose_a_way_of_payment()
    assert selected_phone_page.check_that_way_of_payment_six_months()
    selected_phone_page.view_purchase_details()
    selected_phone_page.go_on_to_purchase()
    sign_in_page = SignInPage(driver)
    sign_in_page.open_sign_in_page()
    assert sign_in_page.check_that_jump_to_sign_in_page_was_completed



