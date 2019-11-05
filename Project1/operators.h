#pragma once
#ifndef OPERATORS_H
#define OPERATORS_H

#include "project1.h"
#include "node.h"

Node* move_right(Node* node, std::pair<int, int> coord);
Node* move_left(Node* node, std::pair<int, int> coord);
Node* move_down(Node* node, std::pair<int, int> coord);
Node* move_up(Node* node, std::pair<int, int> coord);

#endif //OPERATORS_H
