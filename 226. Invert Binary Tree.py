# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.change(root)
        return root

    def change(self, root):
        if(root):
            if(root.left is None and root.right is None):
                pass
            else:
                root.left, root.right = root.right, root.left
                self.change(root.left)
                self.change(root.right)
        