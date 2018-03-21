Feature: Implement a Queue Data Structure
  Describe and implement a Queue data structure
  Using Python as a language

  Scenario: Check if a queue is empty
    Given I have an empty Queue
    When I check if the queue is empty
    Then the result should be True

  Scenario: Peek the first element of an empty queue
    Given I have an empty Queue
    When I peek at the queue
    Then I the result should be None

  Scenario: Peek the first element of a non empty queue
    Given I have an empty Queue
    And I add an element foo to the queue
    And I add an element bar to the queue
    When I peek at the queue
    Then I the result should be foo

  Scenario: Remove an element from the queue
    Given I have an empty Queue
    And I add an element foo to the queue
    And I add an element bar to the queue
    When I remove an element from the queue
    Then the first element of the queue should be bar


