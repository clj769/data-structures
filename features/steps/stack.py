from behave import given, when, then, step
from src.data_structures.stack import Stack


@given("I have an empty stack")
def step_impl(context):
    context.stack = Stack()


@when("I check if the stack is empty")
def step_impl(context):
    context.result = context.stack.is_empty()


@when("I peek at the stack")
def step_impl(context):
    context.result = context.stack.peek()


@step("I push an element {element} to the stack")
def step_impl(context, element):
    context.stack.push(element)


@when("I pop an element from the stack")
def step_impl(context):
    context.result = context.stack.pop()


@then("the first element of the stack should be {element}")
def step_impl(context, element):
    assert context.stack.peek().value == element


@then("I the result should be {result}")
def step_impl(context, result):
    assert context.result.value == result


@then("the result of the peek should be {result}")
def step_impl(context, result):
    assert context.result.value == result


@then("there should be a None result")
def step_impl(context):
    assert context.result is None
