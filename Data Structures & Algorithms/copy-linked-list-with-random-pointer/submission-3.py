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
        oldToCopy = { None : None }

        def dfs(old):
            if old in oldToCopy:
                return oldToCopy[old]
            new = Node(old.val)
            oldToCopy[old] = new
            new.next = dfs(old.next)
            new.random = dfs(old.random)
            return new
        
        return dfs(head)