from behave import given, when, then, step
from src.data_structures.trie import Trie


@then("the trie should contain the word {word}")
def step_impl(context, word):
    assert context.trie.contains(word) is True


@step("the trie should not contain the word {word}")
def step_impl(context, word):
    assert context.trie.contains(word) is not True


@given("I have a trie with the following words")
def step_impl(context):
    context.trie = Trie()
    for row in context.table:
        context.trie.add(row.cells[0])


@when("I remove the word {word}")
def step_impl(context, word):
    context.trie.remove(word)


@when("I retrieve a list with all the possible words")
def step_impl(context):
    context.all_words = context.trie.retrieve_all_words()


@then("this list should contain {number:d} elements")
def step_impl(context, number):
    assert len(context.all_words) == number


@step("this list should contain {word}")
def step_impl(context, word):
    assert word in context.all_words
