"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head is None:
        return None
    
    next_temp_node = head.next
    temp_node = head
    prev_temp_node = None
    
    while True:
        temp_node.next = prev_temp_node
        
        if next_temp_node is None:
            return temp_node
        
        prev_temp_node = temp_node
        temp_node = next_temp_node
        next_temp_node = next_temp_node.next

