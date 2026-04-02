# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        prev = slow.next = None

        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt

        first, second = head, prev

        while second:
            nd1, nd2 = first.next, second.next

            first.next = second
            second.next = nd1

            first, second = nd1, nd2




