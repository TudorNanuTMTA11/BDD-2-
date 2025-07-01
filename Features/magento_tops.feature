Feature: Check that the Tops Women page in the Magento website is working properly and I can sort a product by price,
  position and product name in ascending or descending direction
  Background:
    Given I am on the Magento homepage and I want to sort a product with a particular criteria and direction I want
    @T11 @positiveTesting
    Scenario: I want to sort the products by price in ascending and descending direction
      When I click on Price option
      When I click on descending arrow
      When I click on ascending arrow
      Then I have the products arranged as I wanted