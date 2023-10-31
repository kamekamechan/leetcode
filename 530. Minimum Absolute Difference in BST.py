# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.value_list = []

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.add_value(root)
        min_value = 1000000
        for index, value in enumerate(self.value_list[1:], 1):
            min_value = min(min_value, abs(self.value_list[index-1]-value))
        return min_value

    def add_value(self, root):
        if(root):
            self.add_value(root.left)
            self.value_list.append(root.val)
            self.add_value(root.right)
            

        
