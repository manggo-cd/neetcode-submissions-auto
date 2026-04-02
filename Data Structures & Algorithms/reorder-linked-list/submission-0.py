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

        second_half = slow.next
        prev = slow.next = None

        while second_half:
            temp = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = temp

        # merge now. Prev is now the new head of the second half

        first_half, second_half = head, prev

        while second_half: # since second half is leq first half
            tmp1, tmp2 = first_half.next, second_half.next

            first_half.next = second_half
            second_half.next = tmp1

            first_half, second_half = tmp1, tmp2






        