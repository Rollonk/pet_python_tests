import allure
from allure_commons.types import Severity
from demo_qa_tests.model.pages import registration_form


@allure.tag('Registration form')
@allure.severity(Severity.NORMAL)
@allure.label('Owner', 'Kirill')
@allure.feature("User Registration")
@allure.story('Fill valid data')
@allure.link('https://demoqa.com/automation-practice-form', name='Testing')
def test_sending_practice_form():
    with allure.step("Открыть форму регистрации пользователя"):
        registration_form.open_practise_form()

    with allure.step("Заполнить регистрационную форму валидными данными"):
        registration_form.data_fill(first_name='Kirill', last_name='Moskvin',
                                    user_email='MSK@popamail.com', gender='Male', number='1234567890',
                                    file='resources/test_5.jpeg', year='1990', month='2', day='10',
                                    subjects='English', hobbies='Sports', state='NCR', city='Noida',
                                    address='Нижегородская область')

    with allure.step("Отправить форму регистрации"):
        registration_form.send_form()

    with allure.step("Проверить корректность данных в заполненной форме"):
        registration_form.check_get_form(first_name='Kirill', last_name='Moskvin',
                                         user_email='MSK@popamail.com',
                                         gender='Male',
                                         number='1234567890', file='test_5.jpeg',
                                         date='Date of Birth 10 March,1990', subjects='English', hobbies='Sports',
                                         state='NCR',
                                         city='Noida', address='Нижегородская область')

    with allure.step("Закрыть форму"):
        registration_form.close_form()
