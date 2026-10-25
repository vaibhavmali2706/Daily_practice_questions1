# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        cnt = 0
        temp = head

        while temp:
            cnt += 1
            temp = temp.next

        tar = cnt - n + 1
        if tar == 1:
            return head.next
        temp = head

        for i in range(1, tar - 1):
            temp = temp.next
        temp.next = temp.next.next

        return head

        