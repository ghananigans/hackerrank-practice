"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    if head is None:
        return None
    
    size = 1
    
    temp_node = head
    
    while temp_node.next is not None:
        temp_node = temp_node.next
        size += 1
        
    position_head = size - position - 1
  
    temp_node = head
    
    for i in range(position_head):
        temp_node = temp_node.next
        
    return temp_node.data

