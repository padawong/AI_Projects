#pragma once
#ifndef NODE_H
#define NODE_H

#include <vector>
struct compare;

struct Node {
    Node();
    Node(std::vector<std::vector<int> > &grid_in);

    int heuristic;
    int depth;

    void set_grid(std::vector<std::vector<int> > &grid_in);

    bool operator()(const Node& rhs) {
        return heuristic > rhs.heuristic;
    }
    friend bool operator<(const Node& lhs, const Node& rhs) {
        return lhs.heuristic > rhs.heuristic;
    }
    //bool operator==(const Node& rhs); 
    //bool operator()(const Node& rhs);
    //bool operator>(const Node& rhs);
//        bool operator<(const Node* rhs);
    std::vector<std::vector<int> > grid;
    
    void set_depth(int d);
};

struct compare {
/*    bool operator>(const Node*& lhs, const Node*& rhs) {
        return lhs->heuristic > rhs->heuristic;
    }
*/
    /*
    bool operator>(const Node& lhs, const Node& rhs) {
        return lhs.heuristic < rhs.heuristic;
    }
    */
};

#endif //NODE_H
