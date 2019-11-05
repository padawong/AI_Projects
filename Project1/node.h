#pragma once
#ifndef NODE_H
#define NODE_H

#include <vector>

class Node {
    public:
        Node();
        Node(std::vector<std::vector<int> > &grid_in);
        void set_grid(std::vector<std::vector<int> > &grid_in);
        bool operator==(const Node& rhs);
        std::vector<std::vector<int> > grid;
        int heuristic;
        int depth;
};


#endif //NODE_H
