import pytest
from selene.support.shared import browser


@pytest.fixture()
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture()
def open_browser_for_find(window_size):
    browser.open('https://google.com')


@pytest.fixture()
def open_browser_for_form(window_size):
    browser.open('https://demoqa.com/automation-practice-form')
    # browser.config.driver.maximize_window()
