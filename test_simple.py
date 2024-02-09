from selene.support.shared import browser
from selene import be, have


def test_easy(open_browser_for_find):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_easy_negative(open_browser_for_find):
    browser.element('[name="q"]').should(be.blank).type('vvsshhttll1122ccgg').press_enter()
    browser.element('.card-section').should(have.text('По запросу vvsshhttll1122ccgg ничего не найдено'))


def test_hard(open_browser_for_form):
    browser.element('#firstName').type('yashaka')
    browser.element('#lastName').should(be.blank).type('selene')
    browser.element('#userEmail').should(be.blank).type('yashaka@selene.com')
    browser.element('[for="gender-radio-1"]').should(have.text('Male')).click()
    browser.element('#userNumber').should(be.blank).type('9876543210')
    # browser.element('#dateOfBirthInput').click()
    # browser.element('#react-datepicker__month-select').click()
    # browser.element('#react-datepicker__month-select option[value="2"]').should(have.text('April')).click()
    # browser.element('#react-datepicker__year-select').click()
    # browser.element('#react-datepicker__year-select option[value="1990"]').should(have.text('2005')).click()
    # browser.element('#react-datepicker__day--010').should(have.text('10')).click()
    browser.element('[for="hobbies-checkbox-2"]').should(have.text('Reading')).click()
    # browser.element('#uploadPicture').send_keys("E:/python/ex1/getting-started-python-master/1.png")
    # browser.element('#currentAddress').should(be.blank).type('Address')
    # browser.element('#state').click()
    # browser.element('#react-select-3-option-0').should(have.text('NCR')).click()
    # browser.element('#city').click()
    # browser.element('#react-select-4-option-0').should(have.text('Delhi')).click()
    # browser.element('#submit').click()
    # browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

