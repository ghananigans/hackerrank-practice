"""
 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def RemoveDuplicates(head):
    if head is None:
        return None
    
    temp_node = head
    next_temp_node = head.next
  
    while next_temp_node is not None:
        if next_temp_node.data == temp_node.data:
            temp_node.next = next_temp_node.next
        else:
            temp_node = next_temp_node
            
        next_temp_node = next_temp_node.next
        
    return head

