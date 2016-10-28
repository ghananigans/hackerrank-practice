"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    if root is None:
        return
    
    fringe = list()
    prev = root
    temp_node = None
    
    fringe.append(root)
        
    string_out = ""

    while len(fringe) > 0:
        temp_node = fringe[-1]
        
        if (temp_node.right == prev or temp_node.left == prev) or (temp_node.right is None and temp_node.left is None):
            # Travelling up now or node is a leaf node so print
            fringe.pop()
            string_out += str(temp_node.data) + " "
        else:
            # Not leaf or still going down so add to stack
            if temp_node.right is not None:
                fringe.append(temp_node.right)

            if temp_node.left is not None:
                fringe.append(temp_node.left)
                
        prev = temp_node
           
    print(string_out[:-1])

