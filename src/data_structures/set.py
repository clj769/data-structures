class Set:
    def __init__(self, elements):
        self.elements = elements

    def has(self, element):
        return element in self.elements

    def add(self, element):
        if self.has(element):
            return
        self.elements.append(element)

    def size(self):
        return len(self.elements)

    def remove(self, element):
        for index in range(len(self.elements)):
            if self.elements[index] == element:
                del self.elements[index]

    def clear(self):
        self.elements = []

    def is_empty(self):
        return self.size() == 0
