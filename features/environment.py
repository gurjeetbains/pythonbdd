from utils.driver_setup import BaseSetup

BS = ''


def before_scenario(context, scenario):
    global BS
    BS = BaseSetup()
    driver = BS.setUp()
    context.driver = driver
    print("Before Scenario Hooks")


def after_scenario(context, scenario):
    # Screenshots code will be added here
    global BS
    # print(type(scenario.status)) # This type is Coming as enum so need to convert to String in Next step
    if 'Status.passed' != str(scenario.status):
        BS.takeScreenshot()
        print("Runs")
    BS.tearDown()
    print("After Scenario hooks")
