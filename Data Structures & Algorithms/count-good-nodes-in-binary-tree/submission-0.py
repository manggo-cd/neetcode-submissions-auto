# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countNodes(node: TreeNode, msf: int):
            goodNodes = 0
            
            if node:
                if node.val >= msf:
                    msf = node.val
                    goodNodes += 1

                goodNodes += countNodes(node.left, msf)
                goodNodes += countNodes(node.right, msf)

            return goodNodes

        return countNodes(root, root.val)
        