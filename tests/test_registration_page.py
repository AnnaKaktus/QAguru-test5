from pages.registration_page import RegistrationPage
from data.user import my_test_user


def test_reg_from():
    page = RegistrationPage()
    page.register(my_test_user)

    page.should_have_registered(my_test_user)

    page.close_modal()
