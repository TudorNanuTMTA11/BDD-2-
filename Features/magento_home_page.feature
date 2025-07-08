Feature: Check that the search tab in the Magento website is working properly and I can search any product I want
  Background:
    Given I am on the Magento homepage and I want to initiate the searching products process

    @T7 @positiveTesting
    Scenario: I want to search "Wayfarer Messenger Bag" product
    When I type "Wayfarer Messenger Bag" in the search tab
    When I am redirected to the catalog page
    Then I see the product shown on the page


