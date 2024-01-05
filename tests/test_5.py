from selene import browser, have, be, by
import os.path
from resources import resources

def test_reg_from():
    browser.open('https://demoqa.com/automation-practice-form')

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

    browser.element('#uploadPicture').send_keys(resources.path('kitty.jpeg'))

    browser.element('#currentAddress').should(be.blank).type('Tomsk Any Street, 123')
    browser.element('#react-select-3-input').type('Rajasthan').press_enter()
    browser.element('#react-select-4-input').type('Jaipur').press_enter()
    browser.element('#submit').press_enter()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.all('.table td:nth-child(2)').should(
        have.texts(
            'Anna MyLastName',
            'kaktus54au@gmail.com',
            'Female', '9138018444',
            '09 April,1983',
            'Biology',
            'Sports, Reading',
            'kitty.jpeg',
            'Tomsk Any Street, 123',
            'Rajasthan Jaipur'
        )
    )

    browser.element('#closeLargeModal').press_enter()
