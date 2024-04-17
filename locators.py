from selenium.webdriver.common.by import By


class MestoLocators:
    REGISTRATION_BUTTON_MAIN = (By.XPATH, "//a[text() = 'Регистрация']")
    REGISTRATION_TITLE = (By.XPATH, "//h3[text() = 'Регистрация']")

    LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@id='email']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@type='password' and @id='password']")
    LOGIN_SUBMIT = (By.XPATH, "//button[text() = 'Войти']")

    PROFILE_NAME = (By.XPATH, "//h1[@class = 'profile__title']")

    BURGEST_INGRIDIENTS_BULKO = (By.XPATH, "//[contains(@class, 'burger_ingidients']/div[contains(@class, 'burger_ingridient']'")
