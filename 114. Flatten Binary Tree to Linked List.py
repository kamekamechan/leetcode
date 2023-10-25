# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if(root is not None):
            original = root
            temp_right  = root.right
            root.right = self.flatten(root.left)
            while(root.right is not None):
                root = root.right
            root.right = self.flatten(temp_right)
            original.left = None
            return original