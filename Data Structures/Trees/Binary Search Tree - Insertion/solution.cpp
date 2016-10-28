/*
Node is defined as 

typedef struct node
{
   int data;
   node * left;
   node * right;
}node;

*/


node * insert( node * root, int value )
{
    node * new_node;
    node * n;
    
    new_node = ( node * ) malloc( sizeof( node ) );
    new_node->data = value;
    new_node->left = 0;
    new_node->right = 0;
    
    if ( root == 0 )
    {
        return new_node;
    }
    
    n = root;
    
    while ( 1 )
    {
        if ( value < n->data )
        {
            if ( n->left )
            {
                n = n->left;
            }
            else
            {
                n->left = new_node;
                break;
            }
        }
        else
        {
            if ( n->right )
            {
                n = n->right;
            }
            else
            {
                n->right = new_node;
                break;
            }
        }
    }

   return root;
}

