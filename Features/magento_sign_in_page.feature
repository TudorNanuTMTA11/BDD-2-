Feature: Check that the sign in button in the Magento website is working properly and I can sign in into my account
  Background:
    Given I am on the Magento homepage and I want to initiate the sign in process

    @T2 @positiveTesting
      Scenario: I want to sign in into my account
      When I click "Sign in" option
      When I introduce the email "tudor.nanu10@gmail.com"
      When I introduce the password "Universitate10!"
      When I click the "Sign in" button
      Then I am redirected to "My Account" page

    @T3 @negativeTesting
      Scenario: I don't insert the credentials
      When I click "Sign in" option
      Then I receive the error "This is a required field" for not inserting credentials

    @T4 @negativeTesting
      Scenario: I don't insert the password
      When I introduce the email "tudor.nanu10@gmail.com"
      When I click "Sign in" option
      Then I receive the error: "This is a required field" for not inserting password

    @T5 @negativeTesting
      Scenario: I don't insert the email
      When I introduce the password "Universitate10!"
      When I click "Sign in" option


    @T6 @negativeTesting
      Scenario: I forgot the password
      When I click the button "Forgot your Password?"
      When I introduce the email "tudor.nanu10@gmail.com"
      When I click the button "Reset My Password"
      Then I receive a confirmation message



