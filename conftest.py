import time
import pytest
import tempfile
from selenium.webdriver.chrome.options import Options

from selenium import webdriver


@pytest.fixture()
def setup(request):
    chrome_options = Options()
    user_data_dir = tempfile.mkdtemp()
    chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--headless")  # Optional: run without GUI

    driver = webdriver.Chrome(options=chrome_options)
    driver = webdriver.Chrome()
    driver.get("https://www.flipkart.com/")

    # driver.get("http://192.168.1.1/start.htm")
    driver.maximize_window()
    time.sleep(5)
    request.cls.driver = driver
    yield
    driver.quit()
