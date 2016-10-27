"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    temp_node = head
    history = dict()
    
    while temp_node is not None:
        temp_node = temp_node.next
        
        if temp_node in history:
            return True
        else:
            history[temp_node] = True
        
    return False

