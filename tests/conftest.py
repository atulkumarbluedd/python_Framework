import pytest
from selenium import webdriver
import time

from selenium.webdriver.chrome.service import Service


# from selenium.webdriver.firefox.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default='chrome'
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption('browser_name')
    service = Service()
    if browser_name == 'chrome':
        driver = webdriver.Chrome(service=service)
    if browser_name == 'firefox':
        driver=webdriver.Firefox(service=service)
    driver.maximize_window()
    request.cls.driver = driver  # this is to assign to the existing class driver
    yield
    driver.close()
