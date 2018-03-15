class Hashmap:
    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.size: int = 0
        self.nodes: list = [None] * capacity

    def add(self, key, value) -> None:
        index = self._hash(key)
        node = self.nodes[index]

        while node:
            if node.key == key:
                node.value = value  # update value
                return
            else:  # we need to find the next available index to store our node
                self.nodes[index].chain(Node(key, value))
                self.size += 1
                return

        self.nodes[index] = Node(key, value)
        self.size += 1
        if self.size / self.capacity >= 0.7:
            self.capacity *= 2
            temp_nodes = [None] * self.capacity
            for i in range(0, self.size):
                temp_nodes[i] = self.nodes[i]

            self.nodes = temp_nodes

    def count(self) -> int:
        return self.size

    def get(self, key):
        index = self._hash(key)
        node = self.nodes[index]

        if node is not None:
            while node.key != key:
                if node.next is not None:
                    node = node.next_node()
            return node.value

        return None

    def remove(self, key):
        index = self._hash(key)
        node = self.nodes[index]
        prev = None

        while node is not None:
            if node.key == key:
                break
            prev = node
            node = node.next_node()

        self.size -= 1
        if prev is not None:
            prev.chain(node.next_node())
        else:
            self.nodes[index] = node.next_node()

    def _hash(self, key) -> int:
        hash_value = 0

        for char in key:
            hash_value += ord(char)
        return hash_value % self.capacity


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def chain(self, node: 'Node') -> None:
        self.next = node

    def next_node(self: 'Node') -> 'Node':
        return self.next
