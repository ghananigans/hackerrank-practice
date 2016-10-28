"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    if root is None:
        return
    
    fringe = list()
    fringe.append(root)
    temp_node = root.left
    string_out = ""
   
    
    while len(fringe) > 0:
        while temp_node is not None:
            # Keep going down the left
            fringe.append(temp_node)
            temp_node = temp_node.left
        
        temp_node = fringe.pop()

        string_out += str(temp_node.data) + " "
        
        temp_node = temp_node.right
        
        if temp_node is not None:
            fringe.append(temp_node)
            temp_node = temp_node.left
        
    print(string_out)

