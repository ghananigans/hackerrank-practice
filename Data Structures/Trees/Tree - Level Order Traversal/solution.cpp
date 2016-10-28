/*
struct node
{
    int data;
    node* left;
    node* right;
}*/

#include <queue>

void LevelOrder( node * root )
{
    std::queue< node * > fringe;
    node * n;
    
    if ( root == 0 )
    {
        return;    
    }
    
    fringe.push( root );
    
    while ( fringe.size() )
    {
        n = fringe.front();
        fringe.pop();
        
        if ( n->left )
        {
            fringe.push( n->left );
        }
        
        if ( n->right )
        {
            fringe.push( n->right );
        }
        
        fprintf( stdout, "%s ", std::to_string( n->data).c_str() );
    }
}

