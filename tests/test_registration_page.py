from pages.registration_page import RegistrationPage


def test_reg_from():
    page = RegistrationPage()
    page.open_form()

    page.fill_first_name("Anna")
    page.fill_second_name("MyLastName")
    page.fill_email("kaktus54au@gmail.com")
    page.select_gender("Female")
    page.fill_phone("9138018444")
    page.select_date_of_birth("1983", "April", "09")

    page.fill_subject("Biology")
    page.select_hobbie("Sports")
    page.select_hobbie("Music")

    page.upload_picture("kitty.jpeg")

    page.fill_address("Tomsk Any Street, 123")
    page.select_state("Rajasthan")
    page.select_city("Jaipur")

    page.submit()

    page.should_have_registered(
        first_name="Anna",
        last_name="MyLastName",
        email="kaktus54au@gmail.com",
        gender="Female",
        phone="9138018444",
        day="09",
        month="April",
        year="1983",
        subject="Biology",
        hobby_1="Sports",
        hobby_2="Music",
        picture="kitty.jpeg",
        address="Tomsk Any Street, 123",
        state="Rajasthan",
        city="Jaipur"
    )

    page.close_modal()
