"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        mp = {}

        def dfs(curr):
            if curr in mp:
                return mp[curr]

            copy = Node(curr.val)
            mp[curr] = copy

            for nei in curr.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
        