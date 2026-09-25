# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True
        if root == None:
            return self.balanced
        def maxDepth(root):
            if root is None:
                return 0

            leftDepth = maxDepth(root.left)
            rightDepth = maxDepth(root.right)

            print(leftDepth, rightDepth)
            if abs(leftDepth - rightDepth) > 1:
                self.balanced = False
            
            return (1+ max(leftDepth,rightDepth))
        maxDepth(root)
        return self.balanced