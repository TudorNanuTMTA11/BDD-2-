Feature: Check that the Tops Women page in the Magento website is working properly and I can buy a product with selecting
          the size and color I wish
  Background:
    Given I am on the Magento homepage and I want to purchase a product with a particular size and color I want
    @T10 @positiveTesting
    Scenario: I want to purchase Circe Hooded Ice with size XS and color gray
      When I click on Women option
      When I click on Tops option
      When I click on Hoodies & Sweatshirts option
      When I select XS size on Circe Hooded Ice
      When I select Gray color on Circe Hooded Ice
