Feature: Check that the Sale page in the Magento website is working properly and I can click the images
  in the page
  Background:
    Given I am on the Magento homepage and I want to access the content behind the images
    @T20 @positiveTesting
      Scenario: I want to click a particular image
      When I click on Sale option
      When I am redirected on sale page
      When I click on a particular image
      Then I arrive on sales promotion page