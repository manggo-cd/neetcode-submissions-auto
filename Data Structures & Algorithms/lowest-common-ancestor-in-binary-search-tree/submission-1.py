# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # if both p and q are greater than root, we shift our root
        # same vice versa. 
        # once one is greater and one is smaller, we have found our lowest common ancestor
        cur = root

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right

            if p.val < cur.val and q.val < cur.val:
                cur = cur.left

            else:
                return cur

        