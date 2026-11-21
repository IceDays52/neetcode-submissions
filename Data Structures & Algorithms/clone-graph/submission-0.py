"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {}


        def dfs(curr):
            if curr in visited:
                return visited[curr]

            res = Node(curr.val)

            visited[curr] = res

            for n in curr.neighbors:

                temp = dfs(n)

                res.neighbors.append(temp)

            return res

        return dfs(node)




           