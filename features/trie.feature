Feature: Implement a Trie Data Structure
  Describe and implement a Trie data structure
  Using Python as a language

  Scenario: Add a word to a trie
    Given I have a trie with the following words
      | word |
      | bag  |
      | bus  |
      | bat  |
      | bags |
      | but  |
    Then the trie should contain the word bag
    And the trie should contain the word bat
    And the trie should contain the word bus
    And the trie should not contain the word bugs
    And the trie should not contain the word ba

  Scenario: Remove a word from a trie
    Given I have a trie with the following words
      | word |
      | bag  |
      | bus  |
      | bat  |
      | bags |
      | but  |
    When I remove the word bags
    Then the trie should not contain the word bags
    And the trie should contain the word bag
    And the trie should contain the word but
    And the trie should contain the word bat
    And the trie should contain the word bus

  Scenario: Retrieve all the words from a trie
    Given I have a trie with the following words
      | word |
      | bag  |
      | bus  |
      | bat  |
      | bags |
      | but  |
    When I retrieve a list with all the possible words
    Then this list should contain 5 elements
    And this list should contain bag
    And this list should contain bus
    And this list should contain bat
    And this list should contain bags
    And this list should contain but
