from demo_qa_tests.model.pages import registration_form


def test_sending_practice_form():
    registration_form.open_practise_form()

    # Заполнить регистрационную форму
    registration_form.data_fill(first_name='Kirill', last_name='Moskvin',
                                user_email='MSK@popamail.com', gender='Male', number='1234567890',
                                file='resources/test_5.jpeg', year='1990', month='2', day='10',
                                subjects='English', hobbies='Sports', state='NCR', city='Noida',
                                address='Нижегородская область')

    # Отправить форму регистрации
    registration_form.send_form()

    # Проверить корректность данных в заполненной форме
    registration_form.check_get_form(first_name='Kirill', last_name='Moskvin',
                                     user_email='MSK@popamail.com',
                                     gender='Male',
                                     number='1234567890', file='test_5.jpeg',
                                     date='Date of Birth 10 March,1990', subjects='English', hobbies='Sports', state='NCR',
                                     city='Noida', address='Нижегородская область')

    # Закрыть форму
    registration_form.close_form()

