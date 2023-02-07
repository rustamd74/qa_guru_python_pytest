from selene import have
from selene.support.shared import browser


def open_page():
    browser.open_url('https://github.com/')


def click_button_sign_in():
    browser.element('.HeaderMenu-link--sign-in').click()


def click_hamburger_menu():
    browser.element('.Button-label').click()


def check_header_text():
    browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
