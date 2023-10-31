# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output_list = []
        self.list_len = 0

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.dig(root, 0)
        return self.output_list

    def dig(self, root, depth):
        if(root):
            if(depth >= self.list_len):
                self.output_list.append(root.val)
                self.list_len += 1
            
            self.dig(root.right, depth + 1)
            self.dig(root.left, depth + 1)




        