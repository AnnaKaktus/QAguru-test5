from pages.registration_page import RegistrationPage
from user.user import User

my_test_user = User(
    first_name="Anna",
    last_name="MyLastName",
    email="kaktus54au@gmail.com",
    gender="Female",
    phone="9138018444",
    year="1983",
    month="April",
    day="09",
    subject="Biology",
    hobbies=["Sports", "Music"],
    picture="kitty.jpeg",
    address="Tomsk Any Street, 123",
    state="Rajasthan",
    city="Jaipur",
)


def test_reg_from():
    page = RegistrationPage()
    page.register(my_test_user)

    page.should_have_registered(my_test_user)

    page.close_modal()
