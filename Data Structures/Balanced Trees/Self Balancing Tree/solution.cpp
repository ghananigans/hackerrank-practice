/* Node is defined as :
typedef struct node
{
    int val;
    struct node* left;
    struct node* right;
    int ht;
} node; */

#include <cassert> // assert
#include <algorithm> // std::max
#include <stack> // std::stack

int balance_factor( node * n )
{
    int left_ht;
    int right_ht;
    
    if ( n->left )
    {
        left_ht = n->left->ht;
    }
    else
    {
        left_ht = -1;
    }
    
    if ( n->right )
    {
        right_ht = n->right->ht;
    }
    else
    {
        right_ht = -1;   
    }
    
    return ( left_ht - right_ht );
}

void print_tree_preorder_traversal( node * root )
{
    node * temp_node;
    std::stack< node * > fringe;
    
    fprintf( stdout, "\n" );
    
    if ( !root )
    {
        return;
    }
    
    fringe.push( root );
    
    while ( fringe.size() )
    {
        temp_node = fringe.top();
        fringe.pop();
        
        if ( temp_node->right )
        {
            fringe.push( temp_node->right );
        }
        
        if ( temp_node->left )
        {
            fringe.push( temp_node->left );
        }
        
        fprintf( stdout, "[(%d) BF=%d ht=%d]\n", temp_node->val, balance_factor( temp_node ), temp_node->ht );
    }
}

node * rotate_left_left( node * sub_root )
{
    node * temp_node;
    
    temp_node = sub_root->left;
    sub_root->left = temp_node->right;
    temp_node->right = sub_root;
    
    return ( temp_node );
}

node * rotate_right_right( node * sub_root )
{
    node * temp_node;
    
    temp_node = sub_root->right;
    sub_root->right = temp_node->left;
    temp_node->left = sub_root;
    
    return ( temp_node );
}

node * rotate_left_right( node * sub_root )
{
    sub_root->left = rotate_right_right( sub_root->left );
    return ( rotate_left_left( sub_root ) );
}

node * rotate_right_left( node * sub_root )
{
    sub_root->right = rotate_left_left( sub_root->right );
    return ( rotate_right_right( sub_root ) );
}

node * rebalance_sub_tree( node * sub_root )
{
    int balance_factor_val;
    
    balance_factor_val = balance_factor( sub_root );
    
    if ( balance_factor_val > 1 )
    {
        if ( balance_factor( sub_root->left ) > 0 )
        {
            // LeftLeft
            sub_root = rotate_left_left( sub_root );
        }
        else
        {
            //LeftRight
            sub_root = rotate_left_right( sub_root );
        }
    }
    else if ( balance_factor_val < -1 )
    {
        if (balance_factor( sub_root->right ) > 0 )
        {
            // RightLeft
            sub_root = rotate_right_left( sub_root );
        }
        else
        {
            //RightRight
            sub_root = rotate_right_right( sub_root );
        }
    }
    
    return ( sub_root );
}

int update_heights( node * sub_root )
{
    if ( !sub_root )
    {
        return -1;
    }

    sub_root->ht = 1 + std::max( update_heights( sub_root->left ), update_heights( sub_root->right ) );

    return ( sub_root->ht );
}

node * insert( node * root, int val )
{
    node * new_node;
    
    if ( !root )   
    {
        // Create the new node
        new_node = ( node * ) malloc( sizeof( node ) );
        new_node->val = val;
        new_node->left = 0;
        new_node->right = 0;
        new_node->ht = 0;
        
        // Currently an empty tree so
        // new_node is the root
        return ( new_node );
    }
    
    if ( root->val > val )
    {
        // New node should be at left
        root->left = insert( root->left, val );
    }
    else if (root->val < val )
    {
        // New node should be at right
        root->right = insert( root->right, val );
    }
    else
    {
        // All nodes are distinct as per problem statement
        assert( false );
    }
    
    root = rebalance_sub_tree( root );
    update_heights( root );
    
    //print_tree_preorder_traversal(root);
    
    return ( root ) ;
}

