#include <vector> // std::vector
#include <istream> // std::istream
#include <sstream> // std::stringstream
#include <iostream> // std::cin
#include <algorithm> // std::swap, std::max
#include <stack> // std::stack

typedef struct node 
{
    int num;
    int left;
    int right;
} node;

void print_tree ( 
    std::vector< node > const &tree 
)
{
    int a;
    
    for ( a = 0; a < tree.size(); a++ )
    {
        fprintf( stdout, "Node #%d L:%d R:%d\n", tree[ a ].num, tree[ a ].left, tree[ a ].right );    
    }
    
    fprintf( stdout, "\n" );
}

void print_tree_inorder_traversal(
    std::vector< node > const &tree
)
{
    std::stack< int > fringe;
    int node;
    
    node = 1;
    fringe.push( 1 );
    
    while ( fringe.size() )
    {
        while ( node && tree[ node - 1 ].left )
        {
            fringe.push( tree[ node - 1 ].left );
            node = tree[ node - 1 ].left;
        }
        
        node = fringe.top();
        fringe.pop();
        
        fprintf( stdout, "%d ", node );
        
        node = tree[ node - 1 ].right;
        if ( node )
        {
            fringe.push( node );
        }
    }
    
    fprintf( stdout, "\n" );
}

void tokenize( 
    std::string const &str, 
    std::vector< std::string > &tokens 
)
{
    std::stringstream ss;
    std::string token;
    
    tokens.clear();
    ss.str( str );
    
    while ( std::getline( ss, token, ' ' ) ) {
        tokens.push_back( token );
    }
}

void generate_tree( 
    std::istream &is, 
    std::vector< node > &tree 
)
{
    std::string line;
    unsigned int N;
    unsigned int i;
    int pos_left;
    int pos_right;
    std::vector< std::string > tokens;
    
    // Number of nodes
    std::getline( is, line );
    N = std::stoi( line );
    
    for ( i = 0; i < N; ++i )
    {
        std::getline( is, line );
        
        tokenize( line, tokens );
        
        tree.push_back( node() );
        
        pos_left = std::stoi( tokens[ 0 ] );
        pos_right = std::stoi( tokens[ 1 ] );
        
        tree[ i ].num = i + 1;
        tree[ i ].left = ( pos_left == -1 ) ? 0 : pos_left;
        tree[ i ].right = ( pos_right == -1 ) ? 0 : pos_right;
    }
}

void swap_children( 
    std::vector< node > &tree, 
    int const node_number 
)
{
    std::swap( tree[ node_number - 1 ].left, tree[ node_number - 1 ].right );
}

int get_tree_height( 
    std::vector< node > const &tree, 
    int const node 
)
{
    if ( node )
    {
        return 1 + std::max( 
            get_tree_height( tree, tree[ node - 1 ].left ), 
            get_tree_height( tree, tree[ node - 1 ].right ) 
        );
    }
    else
    {
        return -1;
    }
}

void swap_children_at_depth( 
    std::vector< node > &tree, 
    int const node_number, 
    int const swap_depth, 
    int current_depth 
)
{
    if ( swap_depth == current_depth )
    {
        swap_children( tree, node_number );
    }
    else
    {
        if ( tree[ node_number - 1 ].left )
        {
            swap_children_at_depth( tree, tree[ node_number - 1 ].left, swap_depth, current_depth + 1 );
        }
        
        if ( tree[ node_number - 1 ].right )
        {
            swap_children_at_depth( tree, tree[ node_number - 1 ].right, swap_depth, current_depth + 1 );
        }
    }
}

int main() 
{
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */ 
    std::vector< node > tree;
    std::string line;
    int T;
    int i;
    int K;
    int tree_height;
    int h;
    
    generate_tree( std::cin, tree );
    tree_height = get_tree_height( tree, 1 );
    // print_tree( tree );
    
    std::getline( std::cin, line );
    T = std::stoi( line );
    
    for ( i = 0; i < T; ++i )
    {
        std::getline( std::cin, line );
        K = std::stoi( line );
        h = K;
        
        while ( h <= tree_height )
        {
            swap_children_at_depth( tree, 1, h, 1 );
            // print_tree( tree );
            h += K;
        }
        
        print_tree_inorder_traversal( tree );
    }
    
    return 0;
}

