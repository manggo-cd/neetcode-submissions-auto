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
        dCopy = {None : None}

        curr = head

        while curr:
            deepCopy = Node(curr.val)
            dCopy[curr] = deepCopy
            curr = curr.next

        curr = head
        while curr:
            deepCopy = dCopy[curr]
            deepCopy.next = dCopy[curr.next]
            deepCopy.random = dCopy[curr.random]
            curr = curr.next

        return dCopy[head]