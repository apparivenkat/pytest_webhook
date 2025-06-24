from login import LoginPage
from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username, password", [("tomsmith", "SuperSecretPassword!"), ("abcd", "pass")])
def test_login(driver, username, password):
    loginPageObj = LoginPage(driver)

    loginPageObj.openBrowser(url = "https://the-internet.herokuapp.com/login")
    # loginPageObj.inputUserName("tomsmith")
    loginPageObj.inputUserName(username)
    # loginPageObj.inputPassword("SuperSecretPassword!")
    loginPageObj.inputPassword(password)
    loginPageObj.clickLogin()
    loginPageObj.success_message()
