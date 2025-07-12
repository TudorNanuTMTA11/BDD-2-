Feature: Check that the Checkout page in the Magento website is working properly and I can complete the purchasing process
  Background:
    Given I am on the Magento homepage and I want to complete the purchase product process
    @T10 @positiveTesting
      Scenario: I want to complete the details of the checkout
      When I introduce the company "SC DEKAEM CREWING SRL"
      When I introduce the street address "Str.Dr.C.Hepites 11 bl.C1 sc.1 et.1 ap.4"
      When I introduce the city "Braila"
      When I introduce the state "Florida"
      When I introuce the postal code "81009"
      When I introduce the country "United States"
      When I introduce the phone number "+40720971922"
      When I select the price
      When I click Next button
      When I click Place Order button
      When I click Continue Shopping button
      Then I am redirected to the home page

    @T13 @negativeTesting
      Scenario: I don't insert the email address
        When I click Next button
        Then it appears the message "This is a required field"

    @T14 @negativeTesting
      Scenario: I don't select the shipping method
      When I click next button
      Then it appears the message "The shipping method is missing. Select the shipping method and try again."

    @T15 @positiveTesting
      Scenario: I want to purchase a product by being signed in into my account
      When I am on checkout page
      When I click the sign in option
      When I insert the email "tudor.nanu10@gmail.com"
      When I insert the password "Universitate10!"
      When I click the sign in button
      When I see the shipping address saved
      When I select the price
      When I click Next button
      When I click Place Order button
      When I click Continue Shopping button
      Then I am redirected to the home page

    @T17 @positiveTesting
      Scenario: I want to change the address of the product shipping
      When I am on checkout page
      When I click the sign in option
      When I insert the email "tudor.nanu10@gmail.com"
      When I insert the password "Universitate10!"
      When I click the sign in button
      When I see the shipping address saved
      When I click on New Address button
      When I introduce the company "SC HOTEL TRAIAN SRL"
      When I introduce the street address "Str.Dr.C.Hepites 11 bl.C1 sc.1 et.1 ap.4"
      When I introduce the city "Braila"
      When I introduce the state "Florida"
      When I introuce the postal code "81009"
      When I introduce the country "United States"
      When I introduce the phone number "+40720971922"
      When I click on Ship Here button
      When a new shipping address appears
      When I select the price
      When I click Next button
      When I click Place Order button
      When I click Continue Shopping button
      Then I am redirected to the home page

