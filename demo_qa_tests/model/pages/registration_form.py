import allure
from selene import have
from selene.support.shared import browser
from demo_qa_tests.model.controls.dropdown import dropdown_react
from demo_qa_tests.model.controls.chekboxes import select_checkbox
from demo_qa_tests.model.controls.select_dates_on_the_calendar import select_dates_on_the_calendar
from demo_qa_tests.model.controls.radio_button import select_radio
from demo_qa_tests.utils import allure_attachment
from demo_qa_tests.utils.files_tools import path_file


@allure.step("Открытие формы регистрации")
def open_practise_form():
    browser.open('/automation-practice-form')
    allure_attachment.add_screenshot(browser)


@allure.step("Заполнить форму регистрации")
def data_fill(first_name, last_name, user_email, gender, number,  file, year, month,
              day, subjects, hobbies, state, city, address):
    browser.element('#firstName').type(first_name)  # ввод имени
    browser.element('#lastName').type(last_name)  # ввод фамилии
    browser.element('#userEmail').type(user_email)  # вод эл почты
    select_radio('[name=gender]', gender)
    browser.element('#userNumber').type(number)  # ввод номера телефонов
    browser.element('#uploadPicture').set_value(path_file(file))
    select_dates_on_the_calendar('#dateOfBirthInput', year=year, month=month, day=day)
    browser.element('#subjectsInput').type(subjects).press_enter()
    select_checkbox('.custom-checkbox', hobbies)
    dropdown_react('3', state)
    dropdown_react('4', city)
    browser.element('#currentAddress').type(address)
    allure_attachment.add_screenshot(browser)


@allure.step("Нажать кнопку подтвердить")
def send_form():
    browser.element('#submit').press_enter()
    allure_attachment.add_screenshot(browser)


@allure.step("Проверить итоговые данные в модальном окне после регистрации")
def check_get_form(first_name, last_name, user_email, gender, number, file, date, subjects,
                   hobbies, state, city, address):
    browser.all('.table-responsive').all('tr').element(1).should(have.text(f'{first_name} {last_name}'))
    browser.all('.table-responsive').all('tr').element(2).should(have.text(user_email))
    browser.all('.table-responsive').all('tr').element(3).should(have.text(gender))
    browser.all('.table-responsive').all('tr').element(4).should(have.text(number))
    browser.all('.table-responsive').all('tr').element(5).should(have.text(date))
    browser.all('.table-responsive').all('tr').element(6).should(have.text(subjects))
    browser.all('.table-responsive').all('tr').element(7).should(have.text(hobbies))
    browser.all('.table-responsive').all('tr').element(8).should(have.text(file))
    browser.all('.table-responsive').all('tr').element(9).should(have.text(address))
    browser.all('.table-responsive').all('tr').element(10).should(have.text(f'{state} {city}'))
    allure_attachment.add_screenshot(browser)


@allure.step("Закрыть форму регистрации")
def close_form():
    browser.element('#closeLargeModal').press_enter()
    allure_attachment.add_screenshot(browser)
