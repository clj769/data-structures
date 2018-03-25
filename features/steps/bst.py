from behave import given, when, then
from src.data_structures import BST


@given("I have a BST with the following nodes")
def step_impl(context):
    context.bst = BST()
    for row in context.table:
        context.bst.add(int(row.cells[0]))


@when("I look for the element {element:d}")
def step_impl(context, element):
    context.result = context.bst.contains(element)


@when("I add a new element {element:d}")
def step_impl(context, element):
    context.bst.add(element)


@then("the element {element:d} should be in the BST")
def step_impl(context, element):
    assert context.result == context.bst.contains(element) is True


@when("I get the BST content in order")
def step_impl(context):
    context.ordered_bst = context.bst.get_in_order()


@then("I should get a list of")
def step_impl(context):
    result = []
    for row in context.table:
        result.append(int(row.cells[0]))

    assert result == context.ordered_bst
