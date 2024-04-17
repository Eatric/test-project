import time

import settings
from locators import MestoLocators


class TestMestoRegistration:

    def test_registration(self, driver):
        driver.get(settings.URL + "/signup")

        assert driver.find_element(*MestoLocators.REGISTRATION_TITLE).is_displayed(), "Registration Title does not exist"