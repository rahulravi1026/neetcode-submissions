# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        while n >= 0:
            cur = cur.next
            n -= 1
        
        nth = dummy
        while cur:
            nth = nth.next
            cur = cur.next
        
        nth.next = nth.next.next
        return dummy.next