Feature: Check that the Training page in the Magento website is working properly and I can click the images
  in the page
  Background:
    Given I am on the Magento homepage and I want to access the content behind the images
    @T21 @positiveTesting
      Scenario: I want to click a particular image
      When I click on Training option
      When I am redirected on training page
      When I click on a particular image
      Then I arrive on erin recommends page

    @T22 @positiveTesting
      Scenario: I want to access Video Download page
      When I click on Training option
      When I am redirected on training page
      When I click on Video Download option
      When I am redirected on video download page
      Then I see a message info