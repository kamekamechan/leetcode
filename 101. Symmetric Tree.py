# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if(root is None):
            return None
        elif(root.left is not None and root.right is not None):
            return self.scrutiny(root.left, root.right)
        elif(root.left is None and root.right is None):
            return True
        else:
            return False
        
    def scrutiny(self, p, q):
        if(p is not None and q is not None):
            if(p.val == q.val):
                return True and self.scrutiny(p.left, q.right) and self.scrutiny(p.right, q.left)
            else:
                return False
        elif(p is not None and q is None or p is None and q is not None):
            return False
        else:
            return True