"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def Reverse(head):
    temp_node = head
    prev_temp_node = None
    
    while temp_node:
        temp_node_next = temp_node.next
        temp_node.next = temp_node.prev
        temp_node.prev = temp_node_next
        prev_temp_node = temp_node
        temp_node = temp_node_next
        
    return prev_temp_node

