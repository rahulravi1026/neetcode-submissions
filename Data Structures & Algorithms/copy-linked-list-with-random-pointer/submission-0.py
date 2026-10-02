"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None : None}
        def dfs(old):
            if old in oldToNew:
                return oldToNew[old]
            copy = Node(old.val)
            oldToNew[old] = copy
            copy.next = dfs(old.next)
            copy.random = dfs(old.random)
            return copy

        return dfs(head)