# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        sett = set()

        while curr:
            if curr.val in sett and curr.next is not None:
                return True

            sett.add(curr.val)
            curr = curr.next
        
        return False
            
