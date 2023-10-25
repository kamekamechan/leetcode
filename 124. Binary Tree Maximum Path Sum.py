# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.max_num = -1000

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        root_list = [root]
        while(root_list):
            root = root_list.pop()

            if(root.left is not None and root.right is not None):
                self.max_num = max(self.max_num, root.val + max(0, self.sum_and_check(root.left, 0) + self.sum_and_check(root.right, 0)))
                root_list.extend([root.left, root.right])
            elif(root.left is not None and root.right is None):
                self.max_num = max(self.max_num, root.val, self.sum_and_check(root.left, root.val))
                root_list.append(root.left)
            elif(root.left is None and root.right is not None):
                self.max_num = max(self.max_num, root.val, self.sum_and_check(root.right, root.val))
                root_list.append(root.right)
            else:
                self.max_num = max(self.max_num, root.val)

        return self.max_num

    def sum_and_check(self, root, sum):
        current_sum = sum + root.val
        if(root.left is None and root.right is None):
            return max(sum, current_sum)
    
        elif(root.left is not None and root.right is None):
            return max(sum, current_sum + max(0, self.sum_and_check(root.left, 0)))
        elif(root.left is None and root.right is not None):
            return max(sum, current_sum + max(0, self.sum_and_check(root.right, 0)))
        else:
            return max(sum, current_sum + max(0, self.sum_and_check(root.left, 0), self.sum_and_check(root.right, 0)))
        
        