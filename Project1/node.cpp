#include "node.h"

Node::Node() {
}

Node::~Node() {
    //delete child;
}

Node::Node(std::vector<std::vector<int> > &grid_in) {
    this->grid = grid_in;
    dimension = grid_in.size();
    puzzle_size = dimension*dimension - 1;
    heuristic = 0;
    depth = 0;
    //parent = nullptr;
}

/*
Node::Node(Node* node_in) {
    this->grid = node_in->grid;
    dimension = node_in->dimension;
    puzzle_size = node_in->puzzle_size;
    heuristic = node_in->heuristic;
    depth = node_in->depth;
    parent = node_in->parent;
}
*/

void Node::set_grid(std::vector<std::vector<int> > &grid_in) {
    this->grid = grid_in;
    dimension = grid_in.size();
    puzzle_size = dimension*dimension - 1;
    heuristic = 0;
    depth = 0;
    //parent = nullptr;
}

void Node::set_depth(int d) {
    this->depth = d;
}
