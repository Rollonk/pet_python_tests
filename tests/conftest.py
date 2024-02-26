import allure
import pytest
import requests
from selene.support.shared import browser
# from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from demo_qa_tests.utils import allure_attachment

browser.config.base_url = 'https://demoqa.com'


def send_telegram_resulting_message(url, chat_id, text):
    requests.post(
        url=url,
        json={
            "chat_id": chat_id,
            "text": text
        }
    )


def pytest_addoption(parser: pytest.Parser):
    """Add options to pytest"""
    parser.addoption(
        "--run_type",
        help="Run in cloud on Selenoid or on local computer",
        required=False,
        default="local",
        choices=['local', 'remote'],
    )


# def pytest_configure(config: pytest.Config):
#     """Skip tests for firefox if mobile-only option is True"""
#     if config.getoption("--mobile-only") and config.getoption("browser") == "firefox":
#         raise ValueError("Нет мобильных тестов для firefox")
#     if config.getoption("browser") == "chrome":
#         config.option.browser = "chrome-latest"


@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_call(item: pytest.Item):
    """Allure dynamic title"""
    yield
    allure.dynamic.title(" ".join(item.name.split("_")[1:]).capitalize())


def pytest_sessionfinish(session: pytest.Session):
    """Resulting message in telegram chat"""
    tests_collected = str(session.testscollected)
    tests_failed = str(session.testsfailed)
    telegram_url = "https://api.telegram.org/bot6879650976:AAEDTmYStwt8UNUnEpRPQbtGDskL9qEikic/sendMessage"
    telegram_chat_id = -1002097549979
    link_message = "Ссылка отчет придет после публикации"
    resulting_message = f"Total tests run: {tests_collected}. Failed: {tests_failed}.\n"
    lucky_text = f"✅ All tests were successful\n{link_message}"
    failed_text = f"🚫 {resulting_message}{link_message}"
    # local_text = f"🧐 {resulting_message}Это сообщение о завершении локального запуска"
    # пример строки удаленного запуска:
    # 'pytest --alluredir=allure-results --run_type=remote -n 2'
    args = session.config.args[0]
    local_text = f"🧐 {args}Это сообщение о завершении локального запуска"
    args_bool = '--run_type=remote' in args
    # print(args_bool)
    if args_bool:
    # if session.config.args[0] == 'pytest --alluredir=allure-results --run_type=remote -n 2':
        if tests_failed == 0:
            send_telegram_resulting_message(telegram_url, telegram_chat_id, lucky_text)
        else:
            send_telegram_resulting_message(telegram_url, telegram_chat_id, failed_text)
    else:
        send_telegram_resulting_message(telegram_url, telegram_chat_id, local_text)


@pytest.fixture()
def window_size():
    browser.config.window_width = 1024
    browser.config.window_height = 768


@pytest.fixture()
def open_browser_for_find():
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
def browser_management(request: pytest.FixtureRequest):
    browser.config.timeout = 5
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    if request.config.option.run_type == 'remote':
        #  для безголового режима:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        browser.config.driver_options = options
        # для селеноида:
        # options = Options()
        # selenoid_capabilities = {
        #     "browserName": "chrome",
        #     "browserVersion": "100.0",
        #     "selenoid:options": {
        #         "enableVNC": True,
        #         "enableVideo": True
        #     }
        # }
        # options.capabilities.update(selenoid_capabilities)
        # driver = webdriver.Remote(
        #     command_executor="http://localhost:4444/wd/hub",
        #     options=options)
        # browser.config.driver = driver
    else:
        browser.config.browser_name = 'chrome'  # or 'firefox' or 'edge' or 'opera'
    yield
    allure_attachment.add_html(browser)
    allure_attachment.add_screenshot(browser)
    allure_attachment.add_logs(browser)
    allure_attachment.add_video(browser)
    browser.quit()
