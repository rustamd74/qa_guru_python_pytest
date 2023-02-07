from model.pages import open_page, click_hamburger_menu, click_button_sign_in, check_header_text


def test_desktop_github(config_browser_desktop):
    open_page()
    click_button_sign_in()
    check_header_text()


def test_mobile_github(config_browser_mobile):
    open_page()
    click_hamburger_menu()
    click_button_sign_in()
    check_header_text()
