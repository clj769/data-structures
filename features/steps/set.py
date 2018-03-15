from behave import given, when, then, step
from src.data_structures import Set


@given("there is an empty Set")
def step_impl(context):
    context.set = Set([])


@when("I add an element {element} to the Set")
def step_impl(context, element):
    context.set.add(element)


@then("the Set has the element {element}")
def step_impl(context, element):
    assert context.set.has(element) is True


@then("the size of the Set should be {size:d}")
def step_impl(context, size):
    assert context.set.size() == size


@given('there is Set with a {element} element')
def step_impl(context, element):
    context.set = Set(elements=[element])


@when('I remove an element {element} from the Set')
def step_impl(context, element):
    context.set.remove(element)


@step('I add an element {element} to the Set')
def step_impl(context, element):
    context.set.add(element)


@when("I clear the Set")
def step_impl(context):
    context.set.clear()


@step('the Set should not contain {element}')
def step_impl(context, element):
    assert context.set.has(element) is False


@then("the Set should be empty")
def step_impl(context):
    assert context.set.is_empty() is True
