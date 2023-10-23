class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        tree_node_arr = []
        count_ind = 0
        for i in root:
            if(tree_node_arr == []):
                tree_node_arr.append(TreeNode(val = i))
            else:
                if(tree_node_arr[count_ind].right != None):
                    tree_node_arr.append(TreeNode(val = i))
                    count_ind += 1
                elif(tree_node_arr[count_ind].left == None):
                    tree_node_arr[count_ind].left = (TreeNode(val = i))
                elif(tree_node_arr[count_ind].right == None or tree_node_arr[count_ind].left == "null"):
                    tree_node_arr[count_ind].right = (TreeNode(val = i))
        return ""
    
test = Solution()
print(test.inorderTraversal( root = [1,"null",2,3,4,5,6]))