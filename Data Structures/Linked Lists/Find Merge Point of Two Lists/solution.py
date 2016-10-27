"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 
"""

def FindMergeNode(headA, headB):
    prev = dict()
    
    temp_node_A = headA
    
    while temp_node_A.next is not None:
        prev[temp_node_A.next] = temp_node_A
        temp_node_A = temp_node_A.next
        
    temp_node_B = headB
    
    while temp_node_B.next is not None:
        if temp_node_B.next in prev:
            return temp_node_B.next.data
        
        temp_node_B = temp_node_B.next
        
    assert(false)

