#ifndef PROJECT1_H
#define PROJECT1_H

#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <utility>

void uniform_cost(std::vector< std::vector<int> > grid);
void print_grid(std::vector< std::vector<int> > grid);
std::vector< std::vector<int> > generate_grid(int dimensions);
std::pair<int, int> const find_zero(std::vector<std::vector<int> > &grid);
bool move_right(std::vector<std::vector<int> > &grid, std::pair<int, int> coord);
bool move_left(std::vector<std::vector<int> > &grid, std::pair<int, int> coord);
bool move_down(std::vector<std::vector<int> > &grid, std::pair<int, int> coord);
bool move_up(std::vector<std::vector<int> > &grid, std::pair<int, int> coord);

#endif // PROJECT1_H
