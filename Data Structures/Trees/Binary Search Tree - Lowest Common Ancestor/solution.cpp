/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/

#include <cassert>

node * lca( node * root, int v1, int v2 )
{
    node * temp_node;
    
    temp_node = root;
    
    while ( 1 )
    {
        if ( ( temp_node->data > v1 )  && ( temp_node->data > v2 ) )
        {
            // Both values are less than current node so move to left
            temp_node = temp_node->left;
        }
        else if ( ( temp_node->data < v1 )  && ( temp_node->data < v2 ) )
        {
            // Both values are greater than current node so move to right
            temp_node = temp_node->right;
        }
        else
        {
            return temp_node;
        }
    }

    assert( false );
    return 0;
}

