# Write a Python script using Selenium to automate logging into the website "https://the-internet.herokuapp.com/login" with the following requirements?

# Open the login page in a Chrome browser.
# Maximize the browser window.
# Input the username "tomsmith" and password "SuperSecretPassword!".
# Click the "Login" button.
# Wait for the success message "You logged into a secure area!" to appear.
# Validate that the page contains the success message.
# Close the browser after the test is complete.


# Valid Credentials:
#    •    Username: tomsmith
#    •    Password: SuperSecretPassword!
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.usernameField = (By.ID, "username")
        self.passwordField = (By.ID, "password")
        self.loginButtonField = (By.CLASS_NAME, "radius")
        self.successMessageField = (By.ID, "flash")

    def openBrowser(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def inputUserName(self, username):
        self.driver.find_element(*self.usernameField).send_keys(username)
        print("username entered")

    def inputPassword(self, password):
        self.driver.find_element(*self.passwordField).send_keys(password)
        print("passsword entered")

    def clickLogin(self):
        self.driver.find_element(*self.loginButtonField).click()
        time.sleep(1)


    def success_message(self):
        actual_result = self.driver.find_element(*self.successMessageField).text
        time.sleep(2)
        print(self.driver.find_element(*self.successMessageField).text)
        assert "You logged into a secure area!" in actual_result

