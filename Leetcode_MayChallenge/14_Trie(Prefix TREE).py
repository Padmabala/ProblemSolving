#this takes 128 ms  and 26.9 mb
class Trie:

    def __init__(self):
        self.trie = {}


    def insert(self, word: str) -> None:
        root = self.trie
        for c in word:
            if c not in root:
                root[c ] ={}
            root = root[c]
        root['#'] = '#'

    def search(self, word: str) -> bool:
        # start = self.trie
        # for c in word:
        #     if c not in start:
        #         return False
        #     start = start[c]
        # if '#' in start:
        #     return True
        # return False
        return self.startsWith(word + '#')

    def startsWith(self, prefix: str) -> bool:
        start = self.trie
        for c in prefix:
            if c not in start:
                return False
            start = start[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


#  below code takes 268 ms
# class TrieNode:
#     def __init__(self):
#         self.children=[None]*26
#         self.isEndOfWord=False
# class Trie:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.root=self.getNode()
#     def getNode(self):
#
#         return TrieNode()
#     def _charToIndex(self,ch):
#         return ord(ch)-ord('a')
#
#     def insert(self, word: str) -> None:
#         """
#         Inserts a word into the trie.
#         """
#         currentNode=self.root
#         length=len(word)
#         for level in range(length):
#             index=self._charToIndex(word[level])
#             if not currentNode.children[index]:
#                 currentNode.children[index]=self.getNode()
#             currentNode=currentNode.children[index]
#             print(self.root.children)
#         currentNode.isEndOfWord=True
#
#     def search(self, word: str) -> bool:
#         """
#         Returns if the word is in the trie.
#         """
#         currentNode=self.root
#         for i in range(len(word)):
#             index=self._charToIndex(word[i])
#             if not currentNode.children[index]:
#                 return False
#             currentNode=currentNode.children[index]
#         return currentNode!=None and currentNode.isEndOfWord
#
#     def startsWith(self, prefix: str) -> bool:
#         """
#         Returns if there is any word in the trie that starts with the given prefix.
#         """
#         currentNode=self.root
#         for i in range(len(prefix)):
#             index=self._charToIndex(prefix[i])
#             if not currentNode.children[index]:
#                 return False
#             currentNode=currentNode.children[index]
#         return currentNode!=None
              # # and not currentNode.isEndOfWord  ---------need not check the endOfWord or not for the startsWith given prefix operation. it can/cannot be endOfWord

trie = Trie();

trie.insert("apple");
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))