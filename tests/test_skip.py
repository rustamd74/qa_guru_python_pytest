import pytest
from selene.support.shared import browser

from model.pages import check_header_text, click_button_sign_in, open_page, click_hamburger_menu


@pytest.mark.parametrize('width, height', [pytest.param(1580, 1000, id='Browser size: 1580x1000'),
                                           pytest.param(390, 844, id='Browser size: 390x844')])
def test_github_desktop(width, height):
    if width == 390:
        pytest.skip('This is size for mobile version')
    else:
        browser.config.window_width = width
        browser.config.window_height = height
        open_page()
        click_button_sign_in()
        check_header_text()


@pytest.mark.parametrize('width, height', [pytest.param(1580, 1000, id='Browser size: 1580x1000'),
                                           pytest.param(390, 844, id='Browser size: 390x844')])
def test_github_mobile(width, height):
    if width == 1580:
        pytest.skip('This is size for desktop version')
    else:
        browser.config.window_width = width
        browser.config.window_height = height
        open_page()
        click_hamburger_menu()
        click_button_sign_in()
        check_header_text()
