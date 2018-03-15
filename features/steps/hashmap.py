from behave import given, when, then, step
from src.data_structures import Hashmap


@given("I have an empty Hashmap")
def step_impl(context):
    context.hashmap = Hashmap(10)


@when("I add an element with key {key} and value {value} to the Hashmap")
def step_impl(context, key, value):
    context.hashmap.add(key, value)


@then("the size of the Hashmap should be {size:d}")
def step_impl(context, size):
    assert context.hashmap.count() == size


@given('I have a Hashmap with an element with key {key} and value {value}')
def step_impl(context, key, value):
    context.hashmap = Hashmap(10)
    context.hashmap.add(key, value)


@when('I search for {key}')
def step_impl(context, key):
    result = context.hashmap.get(key)
    context.result = result


@then('I should receive the value {value}')
def step_impl(context, value):
    assert context.result == value


@given("I have a Hashmap with the following elements")
def step_impl(context):
    for row in context.table:
        context.hashmap.add(row['key'], row['value'])


@given("I have a Hashmap with capacity {capacity:d}")
def step_impl(context, capacity):
    context.hashmap = Hashmap(capacity)


@step("I add an element with key {key} and value {value} to the Hashmap")
def step_impl(context, key, value):
    context.hashmap.add(key, value)


@when("I get an element for the key {key}")
def step_impl(context, key):
    context.result = context.hashmap.get(key)


@when("I remove an element {key} from the Hashmap")
def step_impl(context, key):
    context.hashmap.remove(key)
