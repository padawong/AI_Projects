#include "operators.h"

class Node;

Node* move_right(Node* node, std::pair<int, int> coord) {
    if (coord.second == 2) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first).at(coord.second + 1));

    return new_node;
}

Node* move_left(Node* node, std::pair<int, int> coord) {
    if (coord.second == 0) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first).at(coord.second - 1));
    return new_node;
}

Node* move_down(Node* node, std::pair<int, int> coord) {
    if (coord.first == 2) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first + 1).at(coord.second));
    return new_node;
}

Node* move_up(Node* node, std::pair<int, int> coord) {
    if (coord.first == 0) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first - 1).at(coord.second));
    return new_node;
}
