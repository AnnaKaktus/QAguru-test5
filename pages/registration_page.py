from selene import browser, have, be, by
from resources import resources


class RegistrationPage:

    def open_form(self):
        browser.open('/automation-practice-form')
        browser.element('.pattern-backgound').should(have.exact_text('Practice Form')).click()

    def fill_first_name(self, first_name):
        browser.element('#firstName').should(be.blank).type(first_name)

    def fill_second_name(self, second_name):
        browser.element('#lastName').should(be.blank).type(second_name)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def select_gender(self, gender="Male"):
        if gender == "Male":
            gender_selector = 'label[for="gender-radio-1"]'
        else:
            gender_selector = 'label[for="gender-radio-2"]'
        browser.element(gender_selector).click()

    def fill_phone(self, phone):
        browser.element('#userNumber').should(be.blank).type(phone)

    def select_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(by.text(year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(by.text(month)).click()
        browser.element('.react-datepicker__day--0' + day).click()

    def fill_subject(self, subject):
        browser.element('#subjectsInput').should(be.blank).type(subject).press_enter()

    def select_hobbie(self, hobby):
        if hobby == "Sports":
            browser.element("[for='hobbies-checkbox-1']").click()
        elif hobby == "Reading":
            browser.element("[for='hobbies-checkbox-2']").click()
        elif hobby == "Music":
            browser.element("[for='hobbies-checkbox-3']").click()

    def upload_picture(self, picture):
        browser.element('#uploadPicture').send_keys(resources.path(picture))

    def fill_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)

    def select_state(self, state):
        browser.element('#react-select-3-input').type(state).press_enter()

    def select_city(self, city):
        browser.element('#react-select-4-input').type(city).press_enter()

    def submit(self):
        browser.element('#submit').press_enter()

    def close_modal(self):
        browser.element('#closeLargeModal').press_enter()

    def read_modal_header(self):
        return browser.element('.modal-header')

    def read_table_data(self):
        return browser.all('.table td:nth-child(2)')

    def should_have_registered(self, first_name, last_name, email, gender, phone, day, month, year, subject,
                               hobby_1, hobby_2, picture, address, state, city):

        self.read_modal_header().should(have.text("Thanks for submitting the form"))

        self.read_table_data().should(
            have.texts(f'{first_name} {last_name}', email, gender, phone, f'{day} {month},{year}', subject,
                       f'{hobby_1}, {hobby_2}', picture, address, f'{state} {city}'))
