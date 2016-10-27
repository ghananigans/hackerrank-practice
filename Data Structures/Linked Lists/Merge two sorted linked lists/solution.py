"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    temp_node_A = headA
    temp_node_B = headB
    prev_temp_node_A = None
    prev_temp_node_B = None
    
    if temp_node_A is None and temp_node_B is None:
        return None
    elif temp_node_A is None and temp_node_B is not None:
        return temp_node_B
    elif temp_node_A is not None and temp_node_B is None:
        return temp_node_A
    
    return_head = None
    
    # Get head to be returned
    if headA.data < headB.data:
        return_head = headA
    else:
        return_head = headB
    
    # Merge the lists until we get to the end of either list
    while temp_node_A is not None and temp_node_B is not None:
        # If list A node is less than B, then find point where A is jsut under
        # pointer to B, then update next pointer
        if temp_node_A.data < temp_node_B.data:
            while temp_node_A is not None and temp_node_A.data < temp_node_B.data:
                prev_temp_node_A = temp_node_A
                temp_node_A = temp_node_A.next

            prev_temp_node_A.next = temp_node_B
        else:
            while temp_node_B is not None and temp_node_B.data < temp_node_A.data:
                prev_temp_node_B = temp_node_B
                temp_node_B = temp_node_B.next

            prev_temp_node_B.next = temp_node_A
            
    return return_head

