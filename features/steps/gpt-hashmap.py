# from behave import given, when, then
# from src.data_structures import Hashmap
#
# @given('I have an empty Hashmap')
# def step_given_I_have_an_empty_Hashmap(context):
#     context.hashmap = Hashmap(10)
#
# @given('I have a Hashmap with an element with key {key} and value {value}')
# def step_given_I_have_a_Hashmap_with_an_element(context, key, value):
#     context.hashmap = Hashmap(10)
#     context.hashmap.add(key, value)
#
# @given('I have a Hashmap with capacity {capacity}')
# def step_given_I_have_a_Hashmap_with_capacity(context, capacity):
#     context.hashmap = Hashmap(int(capacity))
#
# @given('I have a Hashmap with the following elements')
# def step_given_I_have_a_Hashmap_with_elements(context):
#     context.hashmap = Hashmap(10)
#     for row in context.table:
#         context.hashmap.add(row['key'], row['value'])
#
# @when('I add an element with key {key} and value {value} to the Hashmap')
# def step_when_I_add_an_element_to_the_Hashmap(context, key, value):
#     context.hashmap.add(key, value)
#
# @when('I search for {key}')
# def step_when_I_search_for(context, key):
#     context.result = context.hashmap.get(key)
#
# @when('I remove an element {key} from the Hashmap')
# def step_when_I_remove_an_element_from_the_Hashmap(context, key):
#     context.hashmap.remove(key)
#
# @then('the size of the Hashmap should be {size}')
# def step_then_the_size_of_the_Hashmap_should_be(context, size):
#     assert context.hashmap.count() == int(size), f"Expected {size} but got {context.hashmap.count()}"
#
# @then('I should receive the value {value}')
# def step_then_I_should_receive_the_value(context, value):
#     assert context.result == value, f"Expected {value} but got {context.result}"
#
# @given('I add an element with key foo and value bar to the Hashmap')
# def step_given_I_add_foo_bar_element_to_hashmap(context):
#     context.hashmap.add('foo', 'bar')
#
# @when('I get an element for the key foo')
# def step_when_I_get_element_for_key_foo(context):
#     context.result = context.hashmap.get('foo')
