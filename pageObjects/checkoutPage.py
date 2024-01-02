from selenium.webdriver.common.by import By


class checkoutPage:
    def __init__(self, driver):
        self.driver = driver

    # class variable
    checkout = (By.CLASS_NAME, "test12")

    def chekout(self):
        self.driver.find_element(*checkoutPage.checkout)
