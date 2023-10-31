# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_val_list = {}

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # print(self.node_val_list)
        self.add_node_val(root, 0)
        return [values for values in self.node_val_list.values()]

    def add_node_val(self, root, depth):
        if(root):
            if(depth in self.node_val_list.keys()):
                self.node_val_list[depth].append(root.val)
            else:
                self.node_val_list[depth] = [root.val]
            
            self.add_node_val(root.left, depth + 1)
            self.add_node_val(root.right, depth + 1)
        