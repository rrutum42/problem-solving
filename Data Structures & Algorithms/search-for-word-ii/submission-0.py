class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False
    
    def add(self,word: str):
        node = self
        for c in word:
            if c not in node.child:
                node.child[c] = TrieNode()
            node = node.child[c]
        node.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for w in words:
            root.add(w)

        ROWS, COLS = len(board), len(board[0])
        res,visit = set(),set()

        def dfs(r,c,node,word):
            '''
            if r or c are out of bounds OR
            r,c have already been visited OR
            board r,c does not exist in Trie
            then return False
            '''
            if(
                r<0 or c<0 or r>=ROWS or c>=COLS or
                (r,c) in visit or
                board[r][c] not in node.child
            ):
                return False
            
            visit.add((r,c))
            node = node.child[board[r][c]]
            word += board[r][c]
            if node.isEnd:
                res.add(word)

            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")
        
        return list(res)