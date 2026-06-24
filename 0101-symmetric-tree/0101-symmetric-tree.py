class Solution(object):
    def isSymmetric(self, root):
        def check(l, r):
            if not l and not r:
                return True
            
            if not l or not r:
                return False
            
            if l.val != r.val:
                return False
            
            return check(l.left, r.right) and check(l.right, r.left)

        return check(root.left, root.right)