"""
 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list 
"""
def SortedInsert(head, data):
    if head is None:
        return Node(data, None, None)
    
    # New node infront of head
    if head.data > data:
        new_node = Node(data, head, None)
        head.prev = new_node
        return new_node
    
    # New node in middle
    prev_temp_node = None
    temp_node = head
    
    while temp_node is not None:
        if temp_node.data < data:
            prev_temp_node = temp_node
            temp_node = temp_node.next
        else:
            new_node = Node(data, temp_node, temp_node.prev)
            temp_node.prev.next = new_node
            temp_node.prev = new_node
            return head
    
    # New node at tail
    new_node = Node(data, None, prev_temp_node)
    prev_temp_node.next = new_node
    return head

