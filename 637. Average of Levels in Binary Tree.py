# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.node_val_list = {}

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.add_node_val(root, 0)
        average_list = []
        for values in self.node_val_list.values():
            average_list.append(values[0]/values[1])
        return average_list

    def add_node_val (self, root, depth):
        if(root):
            if(depth in self.node_val_list.keys()):
                self.node_val_list[depth][0] += root.val
                self.node_val_list[depth][1] += 1
            else:
                self.node_val_list[depth] = [root.val, 1]
            
            self.add_node_val(root.right, depth + 1)
            self.add_node_val(root.left, depth + 1)