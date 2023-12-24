from selene import browser
import pytest

@pytest.fixture(scope='function', autouse=True)
def browser_management():
   browser.config.base_url = 'https://demoqa.com'
   browser.config.window_width = 1600
   browser.config.window_height = 900

   yield

   browser.quit()
