import pytest
from faker import Faker
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import settings
from data import MestoServiceTestData
from locators import MestoLocators

fake = Faker()

class TestMestoLogin:

    @pytest.mark.parametrize("locator", [MestoLocators.LOGIN_EMAIL_INPUT, MestoLocators.LOGIN_EMAIL_INPUT])
    def test_login(self, driver, locator):
        email_input = driver.find_element(*locator)
        email_input.send_keys(fake.email())

        password_input = driver.find_element(*MestoLocators.LOGIN_PASSWORD_INPUT)
        password_input.send_keys(MestoServiceTestData.AUTH_PASSWORD)

        submit_button = driver.find_element(*MestoLocators.LOGIN_SUBMIT)
        submit_button.click()

        (WebDriverWait(driver, settings.MAX_WAIT_TIME)
         .until(EC.text_to_be_present_in_element(MestoLocators.PROFILE_NAME,
                                                 'Жак-Ив Кусто')))

        profile_name = driver.find_element(*MestoLocators.PROFILE_NAME)

        assert profile_name.is_displayed() and profile_name.text == 'Жак-Ив Кусто', "Login Failed"
