# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(n1, n2):
            if not n1 and not n2:
                return True

            if not n1 or not n2:
                return False

            if n1.val != n2.val:
                return False

            return sameTree(n1.left, n2.left) and sameTree(n1.right, n2.right)


        def dfs(root, subroot):
            if not root:
                return False

            if sameTree(root, subroot):
                return True
            
            return dfs(root.left, subroot) or dfs(root.right, subroot)

        return dfs(root, subRoot)
