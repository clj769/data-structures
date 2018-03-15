Feature: Implement a Set Data Structure
  Describe and implement a Set data structure
  Using Python as a language

  Scenario: Add element to the Set
    Given there is an empty Set
    When I add an element "foo" to the Set
    Then the Set has the element "foo"

  Scenario: An empty Set should have size zero
    Given there is an empty Set
    Then the Set should be empty

  Scenario: Add another element to the Set
    Given there is Set with a "foo" element
    When I add an element "bar" to the Set
    Then the size of the Set should be 2

  Scenario: Add same element to the Set
    Given there is Set with a "foo" element
    When I add an element "foo" to the Set
    Then the size of the Set should be 1

  Scenario: Remove an element from the Set
    Given there is Set with a "foo" element
    When I remove an element "foo" from the Set
    Then the Set should be empty

  Scenario: Clear all elements from the Set
    Given there is Set with a "foo" element
    And I add an element "bar" to the Set
    When I clear the Set
    Then the Set should be empty
    And the Set should not contain "bar"
    And the Set should not contain "foo"
