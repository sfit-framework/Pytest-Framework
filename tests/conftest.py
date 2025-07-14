import time
import pytest
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    # driver.get("http://192.168.1.1/start.htm")
    driver.maximize_window()
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()
