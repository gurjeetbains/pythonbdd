Feature: Showing off behave

  Scenario: Run a simple test
    Given I open IBSS URL
     When I enter username and password
     Then Clicking login I Should be able to login

  Scenario: Run a simple test 2
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!
