"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(node is None):
            return node
        clone_graph_address = {}
        node_stack = []
        clone_graph_address[node.val] = Node(node.val)
        # print(f"{clone_graph_address=}")
        for neighbor in node.neighbors:
            node_stack.append([node.val, neighbor])

        while(node_stack):
            current_node = node_stack.pop()
            if(current_node[1].val not in clone_graph_address.keys()):
                clone_graph_address[current_node[1].val] = Node(current_node[1].val, [clone_graph_address[current_node[0]]])
                clone_graph_address[current_node[0]].neighbors.append(clone_graph_address[current_node[1].val])
            else:
                # print(f"{current_node[1].val=}")
                clone_graph_address[current_node[1].val].neighbors.append(clone_graph_address[current_node[0]])
                clone_graph_address[current_node[0]].neighbors.append(clone_graph_address[current_node[1].val])
            for neighbor in current_node[1].neighbors:
                if(neighbor.val not in clone_graph_address.keys()):
                    node_stack.append([current_node[1].val, neighbor])

        # print(clone_graph_address)
        # return [neighbor for neighbor in clone_graph_address.values()]
        return clone_graph_address[node.val]
        