#pragma once
#ifndef NODE_H
#define NODE_H

#include <vector>

class Node {
    public:
        Node();
        Node(std::vector<std::vector<int> > &grid_in);

        int heuristic;
        int depth;

        void set_grid(std::vector<std::vector<int> > &grid_in);
        bool operator==(const Node* rhs);
        bool operator()(const Node& rhs);
//        bool operator<(const Node* rhs);
        std::vector<std::vector<int> > grid;
        void set_depth(int d);
};
/*
struct compare {
    bool operator()(const Node& lhs, const Node& rhs) {
        return lhs->heuristic < rhs->heuristic;
    }
};
*/

#endif //NODE_H
