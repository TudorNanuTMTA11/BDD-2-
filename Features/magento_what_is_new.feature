Feature: Check that the What is new page in the Magento website is working properly and I can purchase any product I want
  Background:
    Given I am on the Magento homepage and I want to initiate the purchase product process

    @T9 @positiveTesting
    Scenario: I want to purchase "Wayfarer Messenger Bag" product
    When I click on What is New option
    When I click Add to Cart button on Wayfarer Messenger Bag product
    When I click on action showcart icon
    When I click on Proceed to Checkout button
    Then I am redirected to the checkout page