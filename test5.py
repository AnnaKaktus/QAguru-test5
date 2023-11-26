from selene import browser, have, be, by
import os.path

def test_reg_from():
    browser.open('/automation-practice-form')

    browser.element('.pattern-backgound').should(have.exact_text('Practice Form')).click()

    browser.element('#firstName').should(be.blank).type('Anna')
    browser.element('#lastName').should(be.blank).type('MyLastName')
    browser.element('#userEmail').should(be.blank).type('kaktus54au@gmail.com')
    browser.element('label[for="gender-radio-2"]').click()
    browser.element('#userNumber').should(be.blank).type('9138018444')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(by.text('1983')).click()
    browser.element('.react-datepicker__month-select').click()
    browser.element(by.text('April')).click()
    browser.element('.react-datepicker__day--009').click()

    browser.element('#subjectsInput').should(be.blank).type('Biology').press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('kitty.jpeg'))

    browser.element('#currentAddress').should(be.blank).type('Tomsk Any Street 123')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table-responsive').should(have.text(
        'Anna MylastName' and
        'kaktus54au@gmail.com' and
        'Female' and
        '9138018444' and
        '09 April 1983' and
        'Testing' and
        'Sports' 'Reading' and
        'kitty.jpeg' and
        'Tomsk Any Street, 123' and
        'Rajasthan Jaipur'
    ))

    browser.element('#closeLargeModal').press_enter()




