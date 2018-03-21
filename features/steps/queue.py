from behave import given, when, then, step
from src.data_structures.queue import Queue


@given("I have an empty Queue")
def step_impl(context):
    context.queue = Queue()


@when("I check if the queue is empty")
def step_impl(context):
    context.result = context.queue.is_empty()


@then("the result should be True")
def step_impl(context):
    assert context.result is True


@when("I peek at the queue")
def step_impl(context):
    context.result = context.queue.peek()


@then("I the result should be None")
def step_impl(context):
    assert context.result is None


@step("I add an element {element} to the queue")
def step_impl(context, element):
    context.queue.add(element)


@then("I the result should be {result}")
def step_impl(context, result):
    assert context.result.value == result


@when("I remove an element from the queue")
def step_impl(context):
    context.queue.remove()


@then("the first element of the queue should be {element}")
def step_impl(context, element):
    assert context.queue.peek().value == element
