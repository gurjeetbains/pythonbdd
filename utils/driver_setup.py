from selenium import webdriver
from utils.data_conf import data_setup
from os import getcwd
from datetime import datetime
import allure


class BaseSetup(object):

    def __init__(self):
        self.driver = ''

    def setUp(self):
        dir_path = getcwd()
        if data_setup['browser'] == "firefox":
            self.driver = webdriver.Firefox(executable_path=dir_path + "/drivers/geckodriver")
        elif data_setup['browser'] == 'chrome':
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox(executable_path=dir_path + "/drivers/geckodriver")
        self.driver.implicitly_wait(15)
        self.driver.maximize_window()
        return self.driver

    def tearDown(self):
        self.driver.quit()

    def takeScreenshot(self):
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        allure.attach(self.driver.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        # self.driver.save_screenshot('screenshot-%s.png' % now)

