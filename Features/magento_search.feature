 @T16 @failureTesting
      Scenario: I want to check that the key word I typed in search tab for a product is in the title of the products returned by the search web,
      if not the test should be failed
      When I type "Wayfarer Messenger Bag" in the search tab
      When I click on the search tab to generate the results
      When I am redirected to the catalog page
      Then I see the word "Wayfarer" in the title of the products returned by the search web

