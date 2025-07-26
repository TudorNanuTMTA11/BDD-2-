Feature: Check that the Hoodies and Sweatshirts page in the Magento website is working properly and I sort the products
  in the page
  Background:
    Given I am on the Magento homepage and I want to complete the arrange the products in the page
    @T18 @positiveTesting
      Scenario: I want to arrange the products in list
      When I click on Women option
      When I click on Tops option
      When I click on Hoodies & Sweatshirts option
      When I click the list button
      Then the products are arranged in list

    @T19 @positiveTesting
      Scenario: I want to arrange the products in grid
      When I click on Women option
      When I click on Tops option
      When I click on Hoodies & Sweatshirts option
      When I click the grid button
      Then the products are arranged in grid