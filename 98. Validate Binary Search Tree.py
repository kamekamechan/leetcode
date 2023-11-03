# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.min_value = -2147483649

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return True if self.check(root) else False

    def check(self, root):
        if(root):
            left_check = self.check(root.left)
            if(self.min_value < root.val):
                self.min_value = root.val
            else:
                return False
            if(left_check is not False and self.check(root.right) is not False):
                return True
            else:
                return False
        