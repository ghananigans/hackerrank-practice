"""
 Print elements of a linked list in reverse order as standard output
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def ReversePrint(head):
    if head is None:
        return
    
    temp_node = head
    
    output_string = str(temp_node.data)
    temp_node = temp_node.next
    
    while temp_node is not None:
        output_string = str(temp_node.data) + "\n" + output_string
        temp_node = temp_node.next
        
    print(output_string)

