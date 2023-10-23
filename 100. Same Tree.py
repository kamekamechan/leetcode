# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.scrutiny(p, q)

    def scrutiny(self, p, q):
        if(p is not None and q is not None):
            if(p.val == q.val):
                return True and self.scrutiny(p.left, q.left) and self.scrutiny(p.right, q.right)
            else:
                return False
        elif(p is not None and q is None or p is None and q is not None):
            return False
        else:
            return True
                
        