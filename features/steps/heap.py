from behave import given, when, then
from src.data_structures.heap import Heap


@given("I have a min heap with the following elements")
def step_impl(context):
    context.heap = Heap()
    for row in context.table:
        context.heap.add(int(row['element']))


@when("I add a new element {element:d} to the min heap")
def step_impl(context, element):
    context.heap.add(element)


@then("the min heap should be like {list}")
def step_impl(context, list):
    assert context.heap.data == [int(i) for i in list.split()]


@when("I remove the root from the min heap")
def step_impl(context):
    context.heap.remove_root()
