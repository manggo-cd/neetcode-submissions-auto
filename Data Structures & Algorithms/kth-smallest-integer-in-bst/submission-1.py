# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # run DFS in order traversal and append values to an array so
        # they are sorted in order
        # once done traversing, return the value at index k - 1

        res = []

        def dfs(node):
            if not node:
                return True

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k - 1]