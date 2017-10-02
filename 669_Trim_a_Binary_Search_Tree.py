class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self,root,L,R):
        if root.left:
            left = self.trimBST(root.left,L,R)
        else:
            left = None
        if root.right:
            right = self.trimBST(root.right,L,R)
        else:
            right = None
        if root.val>=L and root.val<=R:
            root.left = left
            root.right = right
            return root
        else:
            return left if left else right




