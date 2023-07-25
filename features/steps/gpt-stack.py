# from behave import given, when, then
# from src.data_structures.stack import Stack
#
# @given("I have an empty stack")
# def step_given_empty_stack(context):
#     context.stack = Stack()
#
# @given('I push an element foo to the stack')
# def step_push_foo(context):
#     context.stack.push('foo')
#
# @given('I push an element bar to the stack')
# def step_push_bar(context):
#     context.stack.push('bar')
#
#
# @when("I check if the stack is empty")
# def step_check_empty(context):
#     context.result = context.stack.is_empty()
#
# @then("the result should be True")
# def step_result_true(context):
#     assert context.result is True
#
# @when("I peek at the stack")
# def step_peek_stack(context):
#     context.result = context.stack.peek()
#
# @then("there should be a None result")
# def step_result_none(context):
#     assert context.result is None
#
# @when('I push an element {element} to the stack')
# def step_push_element(context, element):
#     context.stack.push(element)
#
# @then('the result of the peek should be {element}')
# def step_result_peek(context, element):
#     assert context.stack.peek().value == element
#
# @when('I pop an element from the stack')
# def step_pop_element(context):
#     context.stack.pop()
#
# @then('the first element of the stack should be {element}')
# def step_first_element(context, element):
#     assert context.stack.peek().value == element
