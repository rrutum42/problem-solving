"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        new = {}
        def dfs(node):
            if node in new:
                return new[node]
            
            # add the node to the copy
            copy = Node(node.val)
            new[node] = copy
            neighbors = node.neighbors
            for n in neighbors:
                # add all it's neighbours to the copy
                copy.neighbors.append(dfs(n))
            return copy

        return dfs(node)    
'''
perform dfs and store things in a new node
keep a dictionary adjacency list

'''
        
        