"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 
"""
def print_list(head):
    temp_node = head
        
    while (temp_node is not None):
        print(temp_node.data)
        temp_node = temp_node.next

