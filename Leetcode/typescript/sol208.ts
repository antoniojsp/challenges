
//https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            index = ord(ch) - 97
            if not curr.children[index]:
                curr.children[index] = TrieNode()
            curr = curr.children[index]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            index = ord(ch) - 97
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return curr.isEnd


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            index = ord(ch) - 97
            if not curr.children[index]:
                return False
            curr = curr.children[index]
        return True

# class Trie:
#     def __init__(self):
#         self.root = {}

#     def insert(self, word: str) -> None:
#         curr = self.root
#         for ch in word:
#             if ch not in curr:
#                 curr[ch] = {}
#             curr = curr[ch]
#         curr["#"] = True

#     def search(self, word: str) -> bool:
#         curr = self.root
#         for ch in word:
#             if ch not in curr:
#                 return False
#             curr = curr[ch]
#         return curr.get("#", False)

#     def startsWith(self, prefix: str) -> bool:
#         curr = self.root
#         for chr in prefix:
#             if chr not in curr:
#                 return False
#             curr = curr[chr]
#         return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)