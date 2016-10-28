/*
struct node
{
    int data;
    node* left;
    node* right;
};

*/

void top_view( node * root )
{
    std::string string_out;
    node * n;
 
    if ( root == 0 )
    {
        return;
    }
    
    
    string_out = std::to_string( root->data );
    
    n = root->left;
    
    while ( n )
    {
        string_out = std::to_string( n->data ) + " " + string_out;
        n = n->left;
    }
    
    n = root->right;
    
    while ( n )
    {
        string_out = string_out + " " + std::to_string( n->data );
        n = n->right;
    }
    
    fprintf( stdout, "%s", string_out.c_str() );
}

