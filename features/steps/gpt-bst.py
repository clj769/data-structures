# from behave import given, when, then
# from src.data_structures import BST
#
# @given('I have a BST with the following nodes')
# def step_given_I_have_a_BST(context):
#     context.bst = BST()
#     for row in context.table:
#         context.bst.add(int(row['value']))
#
# @when('I look for the element {element}')
# def step_when_I_look_for_the_element(context, element):
#     context.element = int(element)
#     context.result = context.bst.contains(context.element)
#
# @then('the element {element} should be in the BST')
# def step_then_the_element_should_be_in_BST(context, element):
#     assert context.result == True, f"{element} not found in BST"
#
# @when('I add a new element {element}')
# def step_when_I_add_a_new_element(context, element):
#     context.bst.add(int(element))
#
# @when('I get the BST content in order')
# def step_when_I_get_the_BST_content_in_order(context):
#     context.result = context.bst.get_in_order()
#
# @then('I should get a list of')
# def step_then_I_should_get_a_list_of(context):
#     expected_result = [int(row['result']) for row in context.table]
#     assert context.result == expected_result, f"Expected {expected_result} but got {context.result}"
