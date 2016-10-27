"""
 Merge two linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def CompareLists(headA, headB):
    temp_node_A = headA
    temp_node_B = headB
    
    if temp_node_A is None and temp_node_B is None:
        return 1
    elif temp_node_A is None and temp_node_B is not None:
        return 0
    elif temp_node_A is not None and temp_node_B is None:
        return 0
    
    while True:
        if temp_node_A.data != temp_node_B.data:
            return 0
        
        temp_node_A = temp_node_A.next
        temp_node_B = temp_node_B.next
        
        if temp_node_A is None and temp_node_B is None:
            return 1
        elif temp_node_A is None and temp_node_B is not None:
            return 0
        elif temp_node_A is not None and temp_node_B is None:
            return 0
        
    assert(false)

