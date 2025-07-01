Feature: Check that the Checkout page in the Magento website is working properly and I can complete the purchasing process
  Background:
    Given I am on the Magento homepage and I want to complete the purchase product process
    @T9 @positiveTesting
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