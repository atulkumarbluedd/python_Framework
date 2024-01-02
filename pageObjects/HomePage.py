from selenium.webdriver.common.by import By

from pageObjects.checkoutPage import checkoutPage


class HomePage:

    def __init__(self, driver):  # constructor
        self.driver = driver

    shop = (By.CSS_SELECTOR, 'a[href*="shop"]')

    def shopItem(self):
        self.driver.find_element(*HomePage.shop)
        checkoutpage=checkoutPage(self.driver)
        return checkoutpage


        # * is used to convert the locator into driver.findElement
    # here we are using class name to call shop because it is class variable.
