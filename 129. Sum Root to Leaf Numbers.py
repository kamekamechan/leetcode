# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.return_sum = 0

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if(root is None):
            return False
        self.sum_and_check(root, 0)
        return self.return_sum

    def sum_and_check(self, root, sum):
        current_sum = sum * 10 + root.val
        if(root.left is None and root.right is None):
            self.return_sum += current_sum
    
        elif(root.left is not None and root.right is None):
            return self.sum_and_check(root.left, current_sum)
        elif(root.left is None and root.right is not None):
            return self.sum_and_check(root.right, current_sum)
        else:
            return self.sum_and_check(root.left, current_sum) or self.sum_and_check(root.right, current_sum)
        