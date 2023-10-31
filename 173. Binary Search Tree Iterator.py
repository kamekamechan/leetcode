# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.value_stack = []
        self.make_stack(root)

    def make_stack(self, root):
        if(root):
            self.make_stack(root.right)
            self.value_stack.append(root.val)
            self.make_stack(root.left)

    def next(self) -> int:
        return self.value_stack.pop()

    def hasNext(self) -> bool:
        if(self.value_stack != []):
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()