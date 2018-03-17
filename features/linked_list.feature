Feature: Implement a Linked List Data Structure
  Describe and implement a Linked List data structure
  Using Python as a language

  Scenario: Append a node to a LinkedList
    Given I have an linked list with a head element foo
    When I append a bar element to the linked list
    Then the last element of the linked list should be bar

  Scenario: Prepend a node to a LinkedList
    Given I have an linked list with a head element foo
    When I prepend a bar element to the linked list
    Then the last element of the linked list should be foo

  Scenario: Check if a Linked List contains a value
    Given I have an linked list with a head element foo
    And I append a bar element to the linked list
    Then the linked list should contain the element foo

  Scenario: Delete a value in a Linked List
    Given I have an linked list with a head element foo
    And I append a bar element to the linked list
    When I remove the bar element
    Then the linked list should not contain the element bar
