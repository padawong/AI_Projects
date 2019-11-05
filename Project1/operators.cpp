#include "operators.h"

/* These functions perform the operation if possible
 * assign the new node's depth
 * and return the new node
 *
 * Location of 0 is passed in to avoid recalculating for each operation
 */

struct Node;

Node* move_right(Node* node, std::pair<int, int> coord) {
    if (coord.second == node->dimension - 1) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    new_node->depth = node->depth + 1;
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first).at(coord.second + 1));

    return new_node;
}

Node* move_left(Node* node, std::pair<int, int> coord) {
    if (coord.second == 0) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    new_node->depth = node->depth + 1;
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first).at(coord.second - 1));
    return new_node;
}

Node* move_down(Node* node, std::pair<int, int> coord) {
    if (coord.first == node->dimension - 1) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    new_node->depth = node->depth + 1;
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first + 1).at(coord.second));
    return new_node;
}

Node* move_up(Node* node, std::pair<int, int> coord) {
    if (coord.first == 0) {
        return nullptr;
    }

    Node* new_node = new Node(node->grid);
    new_node->depth = node->depth + 1;
    std::swap(new_node->grid.at(coord.first).at(coord.second), new_node->grid.at(coord.first - 1).at(coord.second));
    return new_node;
}
