Feature: Implement a Stack Data Structure
  Describe and implement a Stack data structure
  Using Python as a language

  Scenario: Check if a stack is empty
    Given I have an empty stack
    When I check if the stack is empty
    Then the result should be True

  Scenario: Peek the first element of an empty stack
    Given I have an empty stack
    When I peek at the stack
    Then there should be a None result

  Scenario: Peek the first element of a non empty stack
    Given I have an empty stack
    And I push an element foo to the stack
    And I push an element bar to the stack
    When I peek at the stack
    Then the result of the peek should be bar

  Scenario: Pop an element from the stack
    Given I have an empty stack
    And I push an element foo to the stack
    And I push an element bar to the stack
    When I pop an element from the stack
    Then the first element of the stack should be foo

  Scenario: Check if push/pop logic is working
    Given I have an empty stack
    When I push an element foo to the stack
    And I push an element bar to the stack
    And I pop an element from the stack
    And I push an element fiz to the stack
    And I push an element liv to the stack
    And I pop an element from the stack
    Then the first element of the stack should be fiz


