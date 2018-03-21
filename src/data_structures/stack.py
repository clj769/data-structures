class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        return self.head is None

    def peek(self):
        return self.head

    def push(self, value):
        node = Node(value)

        if self.head is not None:
            node.next = self.head

        self.head = node

    def pop(self):
        if self.head is None:
            return

        self.head = self.head.next


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
