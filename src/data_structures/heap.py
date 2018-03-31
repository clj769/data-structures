class Heap:
    def __init__(self):
        self.data = []

    def add(self, element: int) -> None:
        self.data.append(element)
        self._percolate_up(len(self.data) - 1)

    def remove_root(self) -> None:
        self.data[0] = self.data[len(self.data) - 1]
        del self.data[len(self.data) - 1]
        self._percolate_down(0)

    def _percolate_down(self, index: int) -> None:
        parent = self.data[index]
        smaller_child_index = self._get_smaller_child_index(index)

        if parent > self.data[smaller_child_index]:
            self._swap(index, smaller_child_index)
            self._percolate_down(smaller_child_index)

    def _percolate_up(self, index: int) -> None:
        if index == 0:
            return

        current = self.data[index]
        parent = self._get_parent(index)

        if current < parent:
            self._swap(index, self._get_parent_index(index))
            self._percolate_up(self._get_parent_index(index))

    def _swap(self, index1: int, index2: int) -> None:
        temp = self.data[index1]
        self.data[index1] = self.data[index2]
        self.data[index2] = temp

    def _get_smaller_child_index(self, parent_index: int) -> int:
        if self._get_right_child(parent_index):
            if self._get_left_child(parent_index) < self._get_right_child(parent_index):
                return self._get_left_child_index(parent_index)
            else:
                return self._get_right_child_index(parent_index)
        else:
            return self._get_left_child_index(parent_index)

    def _get_parent(self, child_index: int):
        return self.data[(child_index - 1) // 2]

    def _get_left_child(self, index: int) -> int:
        if (index * 2) + 1 < len(self.data) - 1:
            return self.data[(index * 2) + 1]

    def _get_right_child(self, index: int) -> int:
        if (index * 2) + 2 < len(self.data) - 1:
            return self.data[(index * 2) + 2]

    @staticmethod
    def _get_parent_index(child_index: int) -> int:
        return (child_index - 1) // 2

    @staticmethod
    def _get_left_child_index(index: int) -> int:
        return (index * 2) + 1

    @staticmethod
    def _get_right_child_index(index: int) -> int:
        return (index * 2) + 2
