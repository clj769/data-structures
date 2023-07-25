# from behave import given, when, then
# from src.data_structures.heap import Heap
#
# @given('I have a min heap with the following elements')
# def step_given_I_have_min_heap_with_elements(context):
#     context.heap = Heap()
#     for row in context.table:
#         context.heap.add(int(row['element']))
#
# @when('I add a new element {element} to the min heap')
# def step_when_I_add_element_to_min_heap(context, element):
#     context.heap.add(int(element))
#
# @then('the min heap should be like {elements}')
# def step_then_min_heap_should_be_like(context, elements):
#     assert ' '.join(map(str, context.heap.data)) == elements
#
# @when('I remove the root from the min heap')
# def step_when_I_remove_root_from_min_heap(context):
#     context.heap.remove_root()
#
