import pytest
from selene.support.shared import browser


@pytest.fixture()
def config_browser_desktop():
    browser.config.window_width = 1580
    browser.config.window_height = 1000


@pytest.fixture()
def config_browser_mobile():
    browser.config.window_width = 390
    browser.config.window_height = 844
