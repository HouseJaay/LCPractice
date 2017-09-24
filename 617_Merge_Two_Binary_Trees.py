class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self,t1,t2):
        def merge(t1,t2,t):
            if t1.left and t2.left:
                t.left = TreeNode(t1.left.val+t2.left.val)
                merge(t1.left,t2.left,t.left)
            elif t1.left:
                t.left = t1.left
            elif t2.left:
                t.left = t2.left

            if t1.right and t2.right:
                t.right = TreeNode(t1.right.val+t2.right.val)
                merge(t1.right,t2.right,t.right)
            elif t1.right:
                t.right = t1.right
            elif t2.right:
                t.right = t2.right
        if t1 and t2:    
            t = TreeNode(t1.val+t2.val)
            merge(t1,t2,t)
        elif t1:
            t = t1
        elif t2:
            t = t2
        else:
            t = None
        return t

