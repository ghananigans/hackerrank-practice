/* 
The structure of the node is

typedef struct node
{
    int freq;
    char data;
    node * left;
    node * right;
    
}node;

*/

#include <cassert>

void decode_huff( node * root,string s )
{
    node * temp_node;
    unsigned int s_index;
    char c;
    
    temp_node = root;
    
    for ( s_index = 0; s_index < s.length(); ++s_index )
    {
        c = s.at( s_index );
        
        if ( c == '0' )
        {
            temp_node = temp_node->left;
        }
        else if ( c == '1' )
        {
            temp_node = temp_node->right;
        }
        else
        {
            // Should never end up here
            assert( false );
        }
        
        if ( !temp_node->left && !temp_node->right )
        {
            fprintf( stdout, "%s", &temp_node->data );
            temp_node = root;
        }
    }
}

