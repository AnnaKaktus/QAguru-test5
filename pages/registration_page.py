from selene import browser, have, be, by
import os.path


class RegistrationPage:

    def register(self, user):
        browser.open('/automation-practice-form')
        browser.element('.pattern-backgound').should(have.exact_text('Practice Form')).click()
        browser.element('#firstName').should(be.blank).type(user.first_name)
        browser.element('#lastName').should(be.blank).type(user.last_name)
        browser.element('#userEmail').should(be.blank).type(user.email)

        if user.gender == "Male":
            gender_selector = 'label[for="gender-radio-1"]'
        else:
            gender_selector = 'label[for="gender-radio-2"]'

        browser.element(gender_selector).click()
        browser.element('#userNumber').should(be.blank).type(user.phone)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(by.text(user.year)).click()
        browser.element('.react-datepicker__month-select').click()
        browser.element(by.text(user.month)).click()
        browser.element('.react-datepicker__day--0' + user.day).click()
        browser.element('#subjectsInput').should(be.blank).type(user.subject).press_enter()

        for hobby in user.hobbies:
            if hobby == "Sports":
                browser.element("[for='hobbies-checkbox-1']").click()
            elif hobby == "Reading":
                browser.element("[for='hobbies-checkbox-2']").click()
            elif hobby == "Music":
                browser.element("[for='hobbies-checkbox-3']").click()

        browser.element('#uploadPicture').send_keys(os.path.abspath(user.picture))
        browser.element('#currentAddress').should(be.blank).type(user.address)
        browser.element('#react-select-3-input').type(user.state).press_enter()
        browser.element('#react-select-4-input').type(user.city).press_enter()
        browser.element('#submit').press_enter()

    def close_modal(self):
        browser.element('#closeLargeModal').press_enter()

    def read_modal_header(self):
        return browser.element('.modal-header')

    def read_table_data(self):
        return browser.all('.table td:nth-child(2)')

    def should_have_registered(self, user):

        self.read_modal_header().should(have.text("Thanks for submitting the form"))

        self.read_table_data().should(
            have.texts(f'{user.first_name} {user.last_name}', user.email, user.gender, user.phone, f'{user.day} {user.month},{user.year}', user.subject,
                       ", ".join(user.hobbies), user.picture, user.address, f'{user.state} {user.city}'))

