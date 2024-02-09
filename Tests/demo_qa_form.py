import os
from selene.support.conditions import have
from selene.support.shared import browser

# установка пути до загружаемого файла
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, './file/test_5.jpeg')


def test_sending_practice_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Kirill')  # ввод имени
    browser.element('#lastName').type('Moskvin')  # ввод фамилии
    browser.element('#userEmail').type('MSK@popamail.com')  # вод эл почты
    browser.element('[for="gender-radio-1"]').click()  # выбор гендера
    browser.element('#userNumber').type('1234567890')  # ввод номера телефонов
    browser.element('#dateOfBirthInput').click()  # открытие формы выбора даты рождения
    browser.element('.react-datepicker__year-select').click()  # открытие выбора года рождения
    browser.element('.react-datepicker__year-select [value="1990"]').click()  # выбор года рождения
    browser.element('.react-datepicker__month-select').click()  # открытие формы выбора месяца рождения
    browser.element('.react-datepicker__month-select [value="2"]').click()  # выбор месяца рождения
    browser.element('.react-datepicker__day--010').click()  # выбор дня рождения
    browser.element('#subjectsInput').type('English').press_enter()  # ввод предмета
    browser.element('[for=hobbies-checkbox-3').click()  # выбор хобби
    browser.element('#uploadPicture').send_keys(file_path)  # загрузка файла
    browser.element('#currentAddress').type('Нижегородская область')  # ввод адрес
    browser.element('#react-select-3-input').type('NCR').press_enter()  # выбор штата
    browser.element('#react-select-4-input').type('Noida').press_enter()  # выбор города
    browser.element('#submit').press_enter()  # отправка формы
    #
    # # проверка соответствия отправленных данных в форме и полученных в итоговой таблицы после отправки заполненной
    # # формы регистрации
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text(
        'Kirill' and
        'Moskvin' and
        'MSK@popamail.com' and
        'Male' and
        '1234567890' and
        '01 March, 1998' and
        'English' and
        'Music' and
        'test_5.jpeg' and
        'Нижегородская область' and
        'NCR Noida'
    ))
