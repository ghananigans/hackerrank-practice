"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""
#This is a "method-only" submission.
#You only need to complete this method.
def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)
    
    nth_node = head
    nth_prev_node = None
    
    for i in range(position):
        nth_prev_node = nth_node
        nth_node = nth_node.next
    
    nth_prev_node.next = Node(data, nth_node)
    
    return head

