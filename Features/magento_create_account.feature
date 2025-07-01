Feature: Check that the create account button in the Magento website is working properly and I can create my account
  Background:
    Given I am on the Magento homepage and I want to initiate the create account process

    @T1 @positiveTesting
      Scenario: I want to create my account
      When I click "Consent" on incognito window
      When I click "Create an Account" option
      When I introduce the first name "Tudor"
      When I introduce the last name "Nanu"
      When I introduce the email "tudor.nanu10@gmail.com"
      When I introduce the password "Universitate10!"
      When I confirm the password "Universitate10!"
      When I click the "Create an Account" button
      Then I am redirected to "My Account" page
