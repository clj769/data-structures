# from behave import given, when, then
# from src.data_structures import Set
#
# @given('there is an empty Set')
# def step_given_empty_set(context):
#     context.set = Set([])
#
# @given('there is Set with a "{element}" element')
# def step_given_set_with_element(context, element):
#     context.set = Set([element])
#
# @given(u'I add an element "bar" to the Set')
# def step_impl(context):
#     context.set.add("bar")
#
#
# @when('I add an element "{element}" to the Set')
# def step_when_add_element_to_set(context, element):
#     context.set.add(element)
#
# @when('I remove an element "{element}" from the Set')
# def step_when_remove_element_from_set(context, element):
#     context.set.remove(element)
#
# @when('I clear the Set')
# def step_when_clear_set(context):
#     context.set.clear()
#
# @then('the Set has the element "{element}"')
# def step_then_set_has_element(context, element):
#     assert context.set.has(element)
#
# @then('the Set should be empty')
# def step_then_set_is_empty(context):
#     assert context.set.is_empty()
#
#
# @then('the size of the Set should be {size:d}')
# def step_then_set_size_is(context, size):
#     assert context.set.size() == size
#
# @then('the Set should not contain "{element}"')
# def step_then_set_does_not_contain_element(context, element):
#     assert not context.set.has(element)
