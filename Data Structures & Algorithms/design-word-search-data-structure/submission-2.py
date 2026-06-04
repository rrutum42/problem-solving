class Node:
    def __init__(self):
        self.child = {} # a -> Node()
        self.isEnd = False
    
    def containsLetter(self, letter: str) -> bool:
        if self.child.get(letter):
            return True
        return False

    def addLetter(self, letter: str):
        self.child[letter] = Node()


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node.containsLetter(char):
                node.addLetter(char)
            node = node.child[char]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(index, node):
            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    # perform dfs for each letter present in child
                    for child in node.child.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:    
                    if not node.containsLetter(char):
                        return False
                    node = node.child[char]
            return node.isEnd
        
        return dfs(0,self.root)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)