# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(n, msf):
            nonlocal count

            if not n:
                return

            if n.val >= msf:
                count += 1

            msf = max(msf, n.val)

            dfs(n.left, msf)
            dfs(n.right, msf)
            return

        dfs(root, root.val)
        return count

            