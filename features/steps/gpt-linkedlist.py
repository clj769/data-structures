# from behave import given, when, then
# from src.data_structures.linked_list import LinkedList
#
# @given('I have an linked list with a head element {head_element}')
# def step_given_I_have_linked_list_with_head(context, head_element):
#     context.linked_list = LinkedList(head_element)
#
# @when('I append a {element} element to the linked list')
# def step_when_I_append_element_to_linked_list(context, element):
#     context.linked_list.append(element)
#
# @then('the last element of the linked list should be {element}')
# def step_then_last_element_of_linked_list_should_be(context, element):
#     assert context.linked_list.get_last().value == element
#
# @when('I prepend a {element} element to the linked list')
# def step_when_I_prepend_element_to_linked_list(context, element):
#     context.linked_list.prepend(element)
#
# @then('the linked list should contain the element {element}')
# def step_then_linked_list_should_contain_element(context, element):
#     assert context.linked_list.contains(element) is True
#
# @when('I remove the {element} element')
# def step_when_I_remove_element(context, element):
#     context.linked_list.remove(element)
#
# @then('the linked list should not contain the element {element}')
# def step_then_linked_list_should_not_contain_element(context, element):
#     assert context.linked_list.contains(element) is False
#
# @given('I append a {element} element to the linked list')
# def step_given_I_append_element_to_linked_list(context, element):
#     context.linked_list.append(element)
