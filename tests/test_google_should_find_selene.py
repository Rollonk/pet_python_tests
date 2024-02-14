import allure
from allure_commons.types import Severity
from selene.support.shared import browser
from selene import be, have
from demo_qa_tests.utils import allure_attachment


@allure.tag('Google and Selene')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kirill')
@allure.feature("Using Google")
@allure.story('User find info about Selene')
@allure.link('https://google.com', name='Testing Google')
def find_selene(open_browser_for_find):
    with allure.step("Ввести в поисковую строку запрос: 'yashaka/selene' и нажать энтер"):
        allure_attachment.add_screenshot(browser)
        browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    with allure.step("Выдача поиска содержит инфо о Селене: 'Selene - User-oriented Web UI browser tests in Python'"):
        browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
        allure_attachment.add_screenshot(browser)
