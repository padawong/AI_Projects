#pragma once
#ifndef PROJECT1_H
#define PROJECT1_H

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <utility>
#include <queue>
#include <list>
#include <algorithm>
#include <string>
#include <functional>
#include "node.h"
#include "operators.h"

Node general_search(std::vector< std::vector<int> > &problem, std::string queueing_function);
void const print_grid(std::vector< std::vector<int> > &grid);
std::vector< std::vector<int> > generate_grid(int dimensions);
std::pair<int, int> const find_zero(std::vector<std::vector<int> > &grid);
void update_queue(Node* node, std::priority_queue<Node> &queue, std::vector<Node*> &open_list, std::vector<Node*> &closed_list, std::string queueing_function);
int node_at(Node* node, std::vector<Node*> &list_in);

#endif // PROJECT1_H
