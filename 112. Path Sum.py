# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if(root is None):
            return False

        return self.sum_and_check(root, 0, targetSum)

    def sum_and_check(self, root, sum, targetSum):
        if(root.left is None and root.right is None):
            if(sum + root.val == targetSum):
                return True
            else:
                return False
    
        elif(root.left is not None and root.right is None):
            return self.sum_and_check(root.left, sum + root.val, targetSum)
        elif(root.left is None and root.right is not None):
            return self.sum_and_check(root.right, sum + root.val, targetSum)
        else:
            return self.sum_and_check(root.left, sum + root.val, targetSum) or self.sum_and_check(root.right, sum + root.val, targetSum)