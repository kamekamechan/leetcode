# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_root_stack = self.search(root, p.val, [])
        q_root_stack = self.search(root, q.val, [])

        # for root in p_root_stack:
        #     print(root.val)
        # print(f"{p_root_stack=}, {q_root_stack=}")
        if(len(p_root_stack) > len(q_root_stack)):
            for index, p_root in enumerate(p_root_stack):
                temp_root = q_root_stack.pop(0)
                if(temp_root.val == p_root.val):
                    if(q_root_stack == []):
                        return temp_root
                else:
                    return p_root_stack[index-1]
        else:
            for index, q_root in enumerate(q_root_stack):
                temp_root = p_root_stack.pop(0)
                if(temp_root.val == q_root.val):
                    if(p_root_stack == []):
                        return temp_root
                else:
                    return q_root_stack[index-1]

    def search(self, root, search_val, root_stack):
        if(root):
            copy_root_stack = copy.copy(root_stack)
            copy_root_stack.append(root)
            if(root.val == search_val):
                return copy_root_stack
            else:
                return self.search(root.left, search_val, copy_root_stack) or self.search(root.right, search_val, copy_root_stack)
        return None


        