"""
 Delete Node at a given position in a linked list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if head is None:
        return None
    
    if position == 0:
        return head.next
    
    nth_node = head
    nth_prev_node = None
    
    for p in range(position):
        nth_prev_node = nth_node
        nth_node = nth_node.next
    
    nth_prev_node.next = nth_node.next
    
    return head

