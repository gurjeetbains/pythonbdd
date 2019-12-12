from behave import given, when, then
from pages.ibss.ibss_home import ibss_home


@given(u'we have behave installed')
def step_impl(context):
    print("test given")


@when(u'we implement 5 tests')
def step_impl(context):
    print('STEP: When we implement 5 tests')


@then(u'behave will test them for us!')
def step_impl(context):
    print('STEP: Then behave will test them for us!')


@given(u'I open IBSS URL')
def step_impl(context):
    ibss_inst = ibss_home(context.driver)
    ibss_inst.ibss_open()
    ibss_inst.enter_login_details()
    context.add = ibss_inst.verify_login()
    print("url opens")


@when(u'I enter username and password')
def step_impl(context):
    print(u'STEP: When I enter username and password')


@then(u'Clicking login I Should be able to login')
def step_impl(context):
    print(u'STEP: Then Clicking login I Should be able to login')
