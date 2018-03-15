Feature: Implement a Hashmap Data Structure
  Describe and implement a Hashmap data structure
  Using Python as a language

  Scenario: Add an element to the Hashmap
    Given I have an empty Hashmap
    When I add an element with key foo and value bar to the Hashmap
    Then the size of the Hashmap should be 1


  Scenario: Search for an element into an the Hashmap
    Given I have a Hashmap with an element with key foo and value bar
    When I search for foo
    Then I should receive the value bar


  Scenario: Adding a value for an already existing key should update the value
    Given I have a Hashmap with an element with key name and value John
    When I add an element with key name and value Paul to the Hashmap
    And I search for name
    Then I should receive the value Paul


  Scenario: Adding a value for an already existing key should not increase the size
    Given I have a Hashmap with an element with key name and value John
    When I add an element with key name and value Paul to the Hashmap
    Then the size of the Hashmap should be 1


  Scenario: Add one more element to a completely filled Hashmap
    Given I have a Hashmap with capacity 3
    And I have a Hashmap with the following elements
      | key         | value           |
      | name        | John            |
      | age         | 30              |
      | nationality | italy           |
  When I add an element with key foo and value bar to the Hashmap
  Then the size of the Hashmap should be 4

  Scenario: Retrieve correct value when there is a collision
    Given I have a Hashmap with an element with key aad and value italy
    And I add an element with key foo and value bar to the Hashmap
    When I get an element for the key foo
    Then I should receive the value bar

  Scenario: Remove an element from the Hashmap
    Given I have a Hashmap with an element with key foo and value bar
    When I remove an element foo from the Hashmap
    Then the size of the Hashmap should be 0

  Scenario: Remove an collided element from the Hashmap
    Given I have a Hashmap with an element with key aad and value italy
    And I add an element with key foo and value bar to the Hashmap
    When I remove an element aad from the Hashmap
    Then the size of the Hashmap should be 1
