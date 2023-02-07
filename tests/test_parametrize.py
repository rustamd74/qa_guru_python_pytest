import pytest
from selene.support.shared import browser

from model.pages import check_header_text, click_button_sign_in, open_page, click_hamburger_menu


@pytest.fixture(params=['desktop', 'mobile'])
def browser_config_param(request):
    open_page()
    if request.param == 'desktop':
        browser.config.window_width = 1580
        browser.config.window_height = 1000
    elif request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844


@pytest.mark.parametrize('browser_config_param', ['desktop'], indirect=True)
def test_desktop_github(browser_config_param):
    open_page()
    click_button_sign_in()
    check_header_text()


@pytest.mark.parametrize('browser_config_param', ['mobile'], indirect=True)
def test_mobile_github(browser_config_param):
    open_page()
    click_hamburger_menu()
    click_button_sign_in()
    check_header_text()
