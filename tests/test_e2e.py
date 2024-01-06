import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") # this fixture we have initialized in the base class so since we have initialized it there
# so we need not to mention explicitly
class TestOne(BaseClass):

    def test_e2e(self, getData): # here u can provide getData or getExcelData based on requirement we can fetch from excel or simple object as well
        logger = self.getLogger()
        # homepage = HomePage(self.driver)
        # checkoutpage = homepage.shopItem()
        # checkoutpage.chekout()
        self.driver.get("https://google.com")
        # self.verifyLinkText("India")  # this is coming from base class
        print(getData['FirstName'])  # this data is coming from fixture provided
        print(getData['LastName'])

        logger.info(f"this test is started execution{getData['HomeTown']}")
        # data driven testing

    # here we have defined this data driven fixture as it is used in this class only
    # if this was getting used by other classes also then we would have defined it in BaseClass or conftest
    @pytest.fixture(params=HomePageData.test_HomePage_Data)
    def getData(self, request):
        return request.param

    @pytest.fixture(params=HomePageData.getExcelData())
    def getExcel_Data(self, request):
        return request.param
