import pytest
from selene.support.shared import browser
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
browser.config.base_url = 'https://demoqa.com'


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
    # remove ad.banners
    browser.execute_script('document.querySelector("footer").remove()')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("#RightSide_Advertisement").remove()')


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.driver_options = options
    browser.config.timeout = 3
    browser.config.browser_name = 'chrome'  # or 'firefox' or 'edge' or 'opera'
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    yield
    browser.quit()
