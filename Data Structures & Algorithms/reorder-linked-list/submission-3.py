# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # hledání středu LL
        dummy = ListNode()
        dummy.next = head

        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # slow ukazuje na střed LL

        # obracení 2. poloviny LL
        curr = slow
        prev = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        # prev ukazuje na head 2. poloviny LL

        # sloučení dvou LL

        curr = head

        while curr and prev:
            tmp = curr.next
            curr.next = prev
            tmp2 = prev.next
            prev.next = tmp

            curr = tmp
            prev = tmp2
            
        return
        