import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") # this fixture we have initialized in the base class so since we have initialized it there
# so we need not to mention explicitly
class TestOne(BaseClass):

    def test_e2e(self):
        self.driver.get("https://google.com")



