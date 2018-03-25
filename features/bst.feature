Feature: Implement a Binary Search Tree (BST) Data Structure
  Describe and implement a BST data structure
  Using Python as a language

  Scenario: Search an element into a BST
    Given I have a BST with the following nodes
      | value |
      | 11    |
      | 19    |
      | 4     |
      | 2     |
      | 20    |
      | 15    |
      | 9     |
    When I look for the element 15
    Then the element 15 should be in the BST

    Given I have a BST with the following nodes
      | value |
      | 11    |
      | 19    |
      | 4     |
      | 2     |
      | 20    |
      | 15    |
      | 9     |
    When I add a new element 14
    Then the element 14 should be in the BST

  Scenario: Print the BST is order
    Given I have a BST with the following nodes
      | value |
      | 11    |
      | 19    |
      | 4     |
      | 2     |
      | 20    |
      | 15    |
      | 9     |
    When I get the BST content in order
    Then I should get a list of
      | result |
      | 2      |
      | 4      |
      | 9      |
      | 11     |
      | 15     |
      | 19     |
      | 20     |
