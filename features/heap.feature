Feature: Implement a Heap Data Structure
  Describe and implement a Heap data structure
  Using Python as a language

  Scenario: Add an element to a heap
    Given I have a min heap with the following elements
      | element |
      | 32      |
      | 10      |
      | 7       |
      | 9       |
      | 12      |
      | 17      |
      | 6       |
      | 3       |
      | 25      |
      | 23      |
      | 20      |
      | 11      |
      | 22      |
    When I add a new element 13 to the min heap
    Then the min heap should be like 3 6 7 9 12 11 10 32 25 23 20 17 22 13

  Scenario: Remove the root element to a heap
    Given I have a min heap with the following elements
      | element |
      | 32      |
      | 10      |
      | 7       |
      | 9       |
      | 12      |
      | 17      |
      | 6       |
      | 3       |
      | 25      |
      | 23      |
      | 20      |
      | 11      |
      | 22      |
    When I remove the root from the min heap
    Then the min heap should be like 6 9 7 22 12 11 10 32 25 23 20 17
