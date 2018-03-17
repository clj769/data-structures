from behave import given, when, then, step
from src.data_structures.linked_list import LinkedList


@given("I have an linked list with a head element {value}")
def step_impl(context, value):
    context.linked_list = LinkedList(value)


@when("I append a {value} element to the linked list")
def step_impl(context, value):
    context.linked_list.append(value)


@step("I append a {value} element to the linked list")
def step_impl(context, value):
    context.linked_list.append(value)


@then("the last element of the linked list should be {value}")
def step_impl(context, value):
    assert context.linked_list.get_last().value == value


@then("the linked list should contain the element {value}")
def step_impl(context, value):
    assert context.linked_list.contains(value) is True


@then("the linked list should not contain the element {value}")
def step_impl(context, value):
    assert context.linked_list.contains(value) is False


@when("I remove the {value} element")
def step_impl(context, value):
    context.linked_list.remove(value)


@when("I prepend a {value} element to the linked list")
def step_impl(context, value):
    context.linked_list.prepend(value)
