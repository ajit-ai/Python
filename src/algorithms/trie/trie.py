class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix):
        return self._find_node(prefix) is not None

    def _find_node(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, node, word, depth):
        if depth == len(word):
            node.is_end = False
            return len(node.children) == 0
        char = word[depth]
        if char not in node.children:
            return False
        should_delete = self._delete(node.children[char], word, depth + 1)
        if should_delete:
            del node.children[char]
            return len(node.children) == 0 and not node.is_end
        return False

    def get_all_words(self, node=None, prefix="", words=None):
        if words is None:
            words = []
        if node is None:
            node = self.root
        if node.is_end:
            words.append(prefix)
        for char, child in sorted(node.children.items()):
            self.get_all_words(child, prefix + char, words)
        return words
