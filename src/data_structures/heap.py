from math import ceil


class Heap:
    def __init__(self):
        self.data = []

    def get_last_index(self) -> int:
        return len(self.data) - 1

    @staticmethod
    def _get_parent_index(child_index: int) -> int:
        return ceil(child_index / 2) - 1

    def add(self, element: int):
        self.data.append(element)
        self._swap(element, self.get_last_index())

    def _swap(self, element, index):
        if index == 0: return

        parent = self.data[Heap._get_parent_index(index)]
        if element < parent:
            self.data[index] = parent
            self.data[Heap._get_parent_index(index)] = element
            self._swap(element, Heap._get_parent_index(index))

        return

        # (index/2) -1 => parent
        # (index*2 +1) => left child
        # (index*2 +2) => right child
