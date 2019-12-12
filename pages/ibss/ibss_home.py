from pages.locators.ibss_loactors import ibss_login_page,ibss_service_page
from utils.data_conf import data_setup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ibss_home:
    def __init__(self, driver):
        self.driver = driver

    def ibss_open(self):
        self.driver.get(data_setup['test_url'])

    def enter_login_details(self):
        self.driver.find_element(*ibss_login_page.username).send_keys("your login")
        self.driver.find_element(*ibss_login_page.password).send_keys("your password")
        self.driver.find_element(*ibss_login_page.login_button).click()

    def verify_login(self):
        el = self.driver.find_element(*ibss_service_page.login_verifier)
        wait = WebDriverWait(self.driver, 18)
        element = wait.until(ec.presence_of_element_located(el))
        return element
