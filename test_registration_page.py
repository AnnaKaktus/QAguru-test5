from pages.registration_page import RegistrationPage
from selene import have

def test_reg_from():
    first_name = "Anna"
    last_name = "MyLastName"
    email = "kaktus54au@gmail.com"
    gender = "Female"
    phone = "9138018444"
    year = "1983"
    month = "April"
    day = "09"
    subject = "Biology"
    hobby_1 = "Sports"
    hobby_2 = "Music"
    picture = "kitty.jpeg"
    address = "Tomsk Any Street, 123"
    state = "Rajasthan"
    city = "Jaipur"

    page = RegistrationPage()
    page.open_form()

    page.fill_first_name(first_name)
    page.fill_second_name(last_name)
    page.fill_email(email)
    page.select_gender(gender)
    page.fill_phone(phone)
    page.select_date_of_birth(year, month, day)

    page.fill_subject(subject)
    page.select_hobbie(hobby_1)
    page.select_hobbie(hobby_2)

    page.upload_picture(picture)

    page.fill_address(address)
    page.select_state(state)
    page.select_city(city)

    page.submit()

    page.read_modat_header().should(have.text("Thanks for submitting the form"))

    page.read_table_data().should(
        have.texts(f"{first_name} {last_name}", email, gender, phone, f"{day} {month},{year}", subject,
                   f"{hobby_1}, {hobby_2}", picture, address, f"{state} {city}")
    )

    page.close_modal()

