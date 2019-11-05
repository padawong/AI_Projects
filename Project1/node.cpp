#include "node.h"

Node::Node() {
}

Node::Node(std::vector<std::vector<int> > &grid_in) {
    this->grid = grid_in;
    heuristic = 0;
    depth = 0;
}

void Node::set_grid(std::vector<std::vector<int> > &grid_in) {
    this->grid = grid_in;
    depth = 0;
}
/*
bool Node::operator==(const Node& rhs) {
    if (grid == rhs.grid) {
        return true;
    }
    else {
        return false;
    }
}
//bool Node::operator<(const Node* rhs) {
bool Node::operator()(const Node& rhs) {
    return heuristic > rhs.heuristic;
}
bool Node::operator>(const Node& rhs) {
    return heuristic < rhs->heuristic;
}
bool Node::operator<(const Node& rhs) {
    return heuristic > rhs->heuristic;
}

*/

void Node::set_depth(int d) {
    this->depth = d;
}
