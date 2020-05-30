'''
Implement Trie (Prefix Tree)
Solution
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings
'''

class Trie:
    def __init__(self):
        self.sons = {}

    def insert(self, word: str) -> None:
        p = self
        for c in word:
            if not c in p.sons:
                p.sons[c] = Trie()
            p = p.sons[c]
        p.sons["#"] = None
        return

    def search(self, word: str) -> bool:
        p = self
        for c in word:
            if not c in p.sons:
                return False
            p = p.sons[c]
        return "#" in p.sons

    def startsWith(self, prefix: str) -> bool:
        p = self
        for c in prefix:
            if not c in p.sons:
                return False
            p = p.sons[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
