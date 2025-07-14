import pytest
from pages.login_page import *
@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_verify_the_allow_block(self):
        loginPage=login_page(self.driver)
        loginPage.click_on_login_btn()
        time.sleep(5)
