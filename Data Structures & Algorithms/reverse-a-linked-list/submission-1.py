# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = head
        if not head:
            return head
        while curr.next:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
        curr.next = prev
        head.next = None
        return curr
