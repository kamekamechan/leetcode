"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def __init__(self):
        self.before_node = []
        self.current_node = []

    def connect(self, root: 'Node') -> 'Node':
        if(root is None):
            return None

        if(root.left is not None):
            self.current_node.append([root,"left"])
        if(root.right is not None):
            self.current_node.append([root,"right"])
        root.next = None
        
        while(self.current_node):
            self.before_node = self.current_node
            self.current_node = []

            while(self.before_node):
                current_before_node, side = self.before_node.pop(0)
                if(side == "left"):
                    if(current_before_node.left.left is not None):
                        self.current_node.append([current_before_node.left,"left"])
                    if(current_before_node.left.right is not None):
                        self.current_node.append([current_before_node.left,"right"])

                    if(self.before_node == []):
                        current_before_node.left.next = None
                    else:
                        if(self.before_node[0][1] == "left"):
                            current_before_node.left.next = self.before_node[0][0].left
                        else:
                            current_before_node.left.next = self.before_node[0][0].right
                else:
                    if(current_before_node.right.left is not None):
                        self.current_node.append([current_before_node.right,"left"])
                    if(current_before_node.right.right is not None):
                        self.current_node.append([current_before_node.right,"right"])

                    if(self.before_node == []):
                        current_before_node.right.next = None
                    else:
                        if(self.before_node[0][1] == "left"):
                            current_before_node.right.next = self.before_node[0][0].left
                        else:
                            current_before_node.right.next = self.before_node[0][0].right
        
        return root
        