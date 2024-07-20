from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_icon()


def test_check_user_name(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_user_name()


def test_check_password(browser):
    swag_labs_page = SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_password()
