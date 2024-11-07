Feature: Login functionality

  Scenario: Successful Login
    Given the user is on the login page
    When the user enters a valid username
    And the user enters a valid password
    And the user clicks the login button
    Then the user should be redirected to the home page
    And the user should be logged in successfully

  Scenario: Unsuccessful Login with Invalid Credentials
    Given the user is on the login page
    When the user enters an invalid username
    And the user enters an invalid password
    And the user clicks the login button
    Then an error message "Invalid username or password." should be displayed
