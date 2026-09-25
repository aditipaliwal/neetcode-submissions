# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    samesies = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def test(p,q):
            if p is None and q is None:
                return
            if (p is not None and q is None) or (p is None and q is not None):
                self.samesies = False
                return
            if p.val != q.val:
                self.samesies = False
                return
            lefty = test(p.left, q.left)
            righty = test(p.right, q.right)
            

        test(p,q)

        return self.samesies



        