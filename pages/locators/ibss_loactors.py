from selenium.webdriver.common.by import By


class ibss_login_page(object):
    username = (By.ID, 'username')
    password = (By.ID, 'password')
    login_button = (By.ID, 'login_button')


class ibss_service_page(object):
    login_verifier = (By.XPATH, "//label[text()='RSP code']")
