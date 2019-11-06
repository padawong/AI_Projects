#pragma once
#ifndef NODE_H
#define NODE_H

#include <vector>

struct Node {
    Node();
    ~Node();
    Node(std::vector<std::vector<int> > &grid_in);
    //Node(Node* node_in);

    //Node* parent;
    //Node* child;
    std::vector<std::vector<int> > grid;
    int dimension;
    int puzzle_size;
    int heuristic;
    int depth;

    void set_grid(std::vector<std::vector<int> > &grid_in);
    void set_depth(int d);

    bool operator()(const Node& rhs) {
        return heuristic > rhs.heuristic;
    }
    friend bool operator<(const Node& lhs, const Node& rhs) {
        return (lhs.depth + lhs.heuristic) > (rhs.depth + rhs.heuristic);
    }
};

#endif //NODE_H
