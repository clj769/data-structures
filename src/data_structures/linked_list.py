class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_next(self) -> 'Node':
        return self.next


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value) -> None:
        node = Node(value)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.get_next() is not None:
            current = current.get_next()

        current.next = node

    def get_last(self) -> Node or None:
        if self.head is None:
            return

        current = self.head
        while current.get_next() is not None:
            current = current.get_next()

        return current

    def contains(self, value) -> bool:
        current = self.head

        while current is not None:
            if current.value == value:
                return True
            current = current.get_next()

        return False

    def prepend(self, value):
        node = Node(value)

        node.next = self.head
        self.head = node

    def remove(self, value) -> None:

        if self.head is None:
            return

        current = self.head

        if current.value == value:
            self.head = self.head.next
            return

        while current.get_next() is not None:
            if current.get_next().value == value:
                current.next = current.get_next().get_next()
                break

        return

