# from behave import given, when, then
# from src.data_structures.queue import Queue
#
# @given('I have an empty queue')
# def step_given_I_have_an_empty_queue(context):
#     context.queue = Queue()
#
# @given('I add an element {element} to the queue')
# def step_given_I_add_element_to_queue(context, element):
#     context.queue.add(element)
#
# @when('I check if the queue is empty')
# def step_when_I_check_if_queue_is_empty(context):
#     context.result = context.queue.is_empty()
#
# @when('I peek at the queue')
# def step_when_I_peek_at_queue(context):
#     context.result = context.queue.peek().value if context.queue.peek() else None
#
# @when('I remove an element from the queue')
# def step_when_I_remove_element_from_queue(context):
#     context.queue.remove()
#
# @then('the result should be {expected_result}')
# def step_then_result_should_be(context, expected_result):
#     if expected_result.lower() == 'true':
#         expected_result = True
#     elif expected_result.lower() == 'false':
#         expected_result = False
#     elif expected_result.lower() == 'none':
#         expected_result = None
#     assert context.result == expected_result, f"Expected: {expected_result}, but was: {context.result}"
#
# @then('the first element of the queue should be {expected_element}')
# def step_then_first_element_of_queue_should_be(context, expected_element):
#     assert context.queue.peek().value == expected_element, f"Expected: {expected_element}, but was: {context.queue.peek().value}"
#
# # Assuming the Queue and Node are defined and imported correctly.
#
# @when('I add an element {element} to the queue')
# def step_when_I_add_element_to_queue(context, element):
#     context.queue.add(element)
