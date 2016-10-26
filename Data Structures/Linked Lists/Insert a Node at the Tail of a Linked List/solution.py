"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    new_node = Node(data, None)
    
    if head is None:
        return new_node
    
    temp_node = head
    
    while temp_node.next is not None:
        temp_node = temp_node.next
        
    temp_node.next = new_node
    
    return head

