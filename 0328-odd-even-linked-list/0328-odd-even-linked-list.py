# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head
        e=head.next
        o=head
        eh=e
        while e is not None and e.next is not None:
            o.next=o.next.next
            o=o.next
            e.next=e.next.next
            e=e.next
        o.next=eh
        return head
        