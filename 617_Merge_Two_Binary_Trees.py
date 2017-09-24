class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self,t1,t2):
        if t1 and t2:    
            t = TreeNode(t1.val+t2.val)
            t.left = self.mergeTrees(t1.left,t2.left)
            t.right = self.mergeTrees(t1.right,t2.right)
            return t
        elif t1:
            return t1
        elif t2:
            return t2
        else:
            return None

