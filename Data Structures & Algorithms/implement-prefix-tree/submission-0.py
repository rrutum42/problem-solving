class Node:
    def __init__(self):
        self.children= [None] * 26
        self.isEnd = False
    
    def getIndex(self, char: str) -> int:
        return ord(char) - ord('a')

    def containsKey(self, char: str) -> bool:
        index = self.getIndex(char)
        return (self.children[index] != None)

    def put(self, char: str):
        index = self.getIndex(char)
        self.children[index] = Node()

class PrefixTree:

    def __init__(self):
        self.root =  Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            index = ord(char)- ord('a')
            if not node.containsKey(char):
                node.put(char)
                # node.children[index] = Node()
            node = node.children[index]
        node.isEnd = True
        

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not node.containsKey(char):
                return False
            node = node.children[ord(char) - ord('a')]
        return node.isEnd


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if not node.containsKey(char):
                return False
            node = node.children[ord(char) - ord('a')]
        return True

