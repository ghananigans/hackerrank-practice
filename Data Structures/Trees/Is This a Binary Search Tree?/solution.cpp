/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
   struct Node {
      int data;
      Node* left;
      Node* right;
   }
*/

#define MAX(a,b) ( ( ( a ) > ( b ) ) ? ( a ) : ( b ) )
#define MIN(a,b) ( ( ( a ) < ( b ) ) ? ( a ) : ( b ) )

bool isSubTreeBST( Node const * const node, int const min, int const max )
{
    bool is_BST_left;
    bool is_BST_right;
    
    //fprintf(stdout,"%d ",node->data);
    
    if ( ( node->data <= min ) || ( node->data >= max ) )
    {
        return false;
    }
    
    if ( node->left )
    {
        is_BST_left = isSubTreeBST( node->left, min, MIN( max, node->data ) );
    }
    else
    {
        is_BST_left = true;
    }
    
    if ( node->right )
    {
        is_BST_right = isSubTreeBST( node->right, MAX( min, node->data ), max );
    }
    else
    {
        is_BST_right = true;
    }
    
    return is_BST_left && is_BST_right; 
}

bool checkBST( Node const * const root ) 
{
    return isSubTreeBST( root, -1, 10001 );
}

