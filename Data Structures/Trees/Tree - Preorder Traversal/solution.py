"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    if root is None:
        return
    
    fringe = list()
    
    string_output = str(root.data)
    
    if root.right is not None:
        fringe.append(root.right)
    
    if root.left is not None:
        fringe.append(root.left)
    
    temp_node = None
    
    while len(fringe) > 0:
        temp_node = fringe.pop()
        
        string_output += " " + str(temp_node.data)
        
        if temp_node.right is not None:
            fringe.append(temp_node.right)

        if temp_node.left is not None:
            fringe.append(temp_node.left)
            
            
    print(string_output)

