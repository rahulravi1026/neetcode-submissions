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
        # oldToCopy = { None : None }

        # def dfs(old):
        #     if old in oldToCopy:
        #         return oldToCopy[old]
        #     new = Node(old.val)
        #     oldToCopy[old] = new
        #     new.next = dfs(old.next)
        #     new.random = dfs(old.random)
        #     return new
        
        # return dfs(head)

        # oldToCopy = defaultdict(lambda : Node(0))
        # oldToCopy[None] = None
        
        # cur = head
        # while cur:
        #     oldToCopy[cur].val = cur.val
        #     oldToCopy[cur].next = oldToCopy[cur.next]
        #     oldToCopy[cur].random = oldToCopy[cur.random]
        #     cur = cur.next
        
        # return oldToCopy[head]

        if not head:
            return None

        # Create merged version of list
        l1 = head
        while l1:
            l2 = Node(l1.val)
            l2.next = l1.next
            l1.next = l2
            l1 = l2.next
        
        # Assign randoms for l2 nodes
        l1 = head
        while l1:
            if l1.random:
                l1.next.random = l1.random.next
            l1 = l1.next.next
        
        # Extract l2 list from merged
        l1 = head
        newHead = head.next
        while l1:
            l2 = l1.next
            l1.next = l1.next.next
            if l2.next:
                l2.next = l2.next.next
            l1 = l1.next

        return newHead



