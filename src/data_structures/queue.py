class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def peek(self):
        return self.head

    def add(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node

        if self.tail is not None:
            self.tail.next = node

        self.tail = node

    def remove(self):
        if self.head is None:
            return

        self.head = self.head.next


class Node:
    next = None

    def __init__(self, value):
        self.value = value
        self.next = None
