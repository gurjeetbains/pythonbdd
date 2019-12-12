from selenium import webdriver
from os import getcwd
from os import path
import logging
import logging.config as cons


# File logger
def file_logger():
    log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logginconf.conf')
    cons.fileConfig(log_file_path)
    logger = logging.getLogger("Anything can go here")
    # This reduces the messages we have to type
    logger.debug("Message")
    logger.warning("warning message")
    logger.error("error")
    logger.critical("full failure")


# Console logger created
def console_logger():
    # Best Practice
    # Create a logger object Console Handlers
    logger = logging.getLogger("Test Logger")
    logger.setLevel(logging.INFO)
    # Have a handler to handle console logger properties
    chandler = logging.StreamHandler()
    chandler.setLevel(logging.INFO)
    # Formatter object to see what type of data entry we are making
    formatter = logging.Formatter("%(asctime)s -%(name)s %(levelname)s: %(message)s",
                                  datefmt="%m-%d-%Y %I:%M:%S %p")
    # Add formatter to console handler
    chandler.setFormatter(formatter)
    # Add Handler to the console logger
    logger.addHandler(chandler)

    # This reduces the messages we have to type
    logger.debug("Message")
    logger.warning("warning message")
    logger.error("error")
    logger.critical("full failure")


# Basic logging in the application
def basic_console_usage():
    """
       Logging Levels
       Debug
       Info
       Warning
       Error
       Critical
       """
    # Basic usage
    logging.basicConfig(format="%(asctime)s: %(levelname)s: %(message)s",
                        filename="test.log",
                        level=logging.DEBUG,
                        datefmt="%m-%d-%Y %I:%M:%S %p")
    logging.warning("Test")


try:
    dir_path = getcwd()
    # Way to run without adding executable in the path file
    # Otherwise copy the driver in bin folder in linux and it will work fine
    driver = webdriver.Firefox(executable_path=dir_path + "/drivers/geckodriver")
    driver.get("https://ibss-test.dev.enable.net.nz/login")
    driver.find_element_by_id("username").send_keys("gurjeet.bains@enable.et.nz")
    driver.find_element_by_id("password").send_keys("Manvi&123456")
    driver.find_element_by_id("login_button")
    # Asserting Library Default one it is there
    assert True == True
    # Logging Library Default library that is available
    file_logger()
    driver.quit()
except Exception as ex:
    print("assertion failed")
    # template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    # message = template.format(type(ex).__name__, ex.args)
    print(type(ex))
