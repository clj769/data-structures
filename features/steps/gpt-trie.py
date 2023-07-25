# from src.data_structures import Trie
# from behave import given, when, then
#
# @given('I have a trie with the following words')
# def step_impl(context):
#     context.trie = Trie()
#     for row in context.table:
#         context.trie.add(row['word'])
#
# @when('I remove the word {word}')
# def step_impl(context, word):
#     context.trie.remove(word)
#
# @when('I retrieve a list with all the possible words')
# def step_impl(context):
#     context.words = context.trie.retrieve_all_words()
#
# @then('the trie should contain the word {word}')
# def step_impl(context, word):
#     assert context.trie.contains(word)
#
# @then('the trie should not contain the word {word}')
# def step_impl(context, word):
#     assert not context.trie.contains(word)
#
# @then('this list should contain {n} elements')
# def step_impl(context, n):
#     assert len(context.words) == int(n)
#
# @then('this list should contain {word}')
# def step_impl(context, word):
#     assert word in context.words
