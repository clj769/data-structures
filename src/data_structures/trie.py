from typing import Optional


class Trie:
    def __init__(self):
        self.root = Node(char=None, is_word=False)

    def add(self, word: str) -> None:
        current = self.root
        is_end_of_word = False

        for i in range(0, len(word)):
            char = word[i]
            if i == len(word) - 1:
                is_end_of_word = True

            if not current.children:
                node_to_insert = Node(char, is_end_of_word)
                current.add_child(node_to_insert)
                current = node_to_insert
                continue

            if char not in current.children:
                node_to_insert = Node(char, is_end_of_word)
                current.add_child(node_to_insert)
                current = node_to_insert
            else:
                current = current.children[char]

    def contains(self, word: str) -> bool:
        current = self.root

        for char in word:
            if not current.children:
                return False

            if char in current.children:
                current = current.children[char]
                continue
            else:
                return False

        if not current.is_word:
            return False

        return True

    def remove(self, word: str) -> None:
        current = self.root

        for i in range(0, len(word)):
            char = word[i]
            is_end_of_word = False

            if i == len(word) - 1:
                is_end_of_word = True

            if char in current.children:
                if current.children[char].is_word and is_end_of_word:
                    current.children[char].is_word = False
                    return
                current = current.children[char]
            else:
                return

    def retrieve_all_words(self) -> list:
        return self._retrieve_all_words(self.root, '', [])

    def _retrieve_all_words(self, current: 'Node', word: str, words: list) -> list:
        for child in current.children.values():
            word = word + child.char
            if child.is_word:
                words.append(word)

            if child.children:
                self._retrieve_all_words(child, word, words)
                word = word[:-1]
                continue

            word = word[:-1]

        return words


class Node:
    def __init__(self, char: Optional[str], is_word: bool):
        self.char = char
        self.is_word = is_word
        self.children = {}

    def add_child(self, node: 'Node'):
        self.children[node.char] = node
