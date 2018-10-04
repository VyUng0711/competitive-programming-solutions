# https://leetcode.com/problems/implement-trie-prefix-tree/description/

class Node:
    
    def __init__(self):
        self.word_end = 0
        self.children = dict()
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                temp.children[ch] = Node()
            temp = temp.children[ch]
        temp.word_end += 1
        
                
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        temp = self.root
        for ch in word:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        if temp.word_end > 0:
            return True
        else:
            return False
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        temp = self.root
        for ch in prefix:
            if ch not in temp.children:
                return False
            temp = temp.children[ch]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
