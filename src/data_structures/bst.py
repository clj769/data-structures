class BST:
    def __init__(self):
        self.root = None
        self.order = []

    def add(self, element: int) -> None:
        if self.root is None:
            self.root = Node(element)
            return

        self._add(self.root, element)

    def _add(self, current: 'Node', element: int) -> None:
        if current.value > element:
            if current.left_child is None:
                current.left_child = Node(element)
                return
            self._add(current.left_child, element)

        if current.value < element:
            if current.right_child is None:
                current.right_child = Node(element)
                return
            self._add(current.right_child, element)

    def contains(self, element: int) -> bool:
        current = self.root

        if current.value == element:
            return True

        if self.root.value > element:
            current = self.root.left_child
        if self.root.value < element:
            current = self.root.right_child

        return self._contains(current, element)

    def _contains(self, current: 'Node', element: int) -> bool:
        if current.value == element:
            return True

        if current.value > element:
            current = current.left_child or None
        elif current.value < element:
            current = current.right_child or None

        if current is None:
            return False

        return self._contains(current, element)

    def get_in_order(self) -> list:
        self._get_in_order(self.root)

        return self.order

    def _get_in_order(self, current: 'Node'):
        if current.left_child:
            self._get_in_order(current.left_child)

        self.order.append(current.value)

        if current.right_child:
            self._get_in_order(current.right_child)


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left_child = None
        self.right_child = None
