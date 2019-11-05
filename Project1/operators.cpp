#include "project1.h"

bool move_right(std::vector<std::vector<int> > &grid, std::pair<int, int> coord) {
    if (coord.second == 2) {
        return false;
    }

    std::swap(grid.at(coord.first).at(coord.second), grid.at(coord.first).at(coord.second + 1));
    return true;
}

bool move_left(std::vector<std::vector<int> > &grid, std::pair<int, int> coord) {
    if (coord.second == 0) {
        return false;
    }

    std::swap(grid.at(coord.first).at(coord.second), grid.at(coord.first).at(coord.second - 1));
    return true;
}

bool move_down(std::vector<std::vector<int> > &grid, std::pair<int, int> coord) {
    if (coord.first == 2) {
        return false;
    }

    std::swap(grid.at(coord.first).at(coord.second), grid.at(coord.first + 1).at(coord.second));
    return true;
}

bool move_up(std::vector<std::vector<int> > &grid, std::pair<int, int> coord) {
    if (coord.first == 0) {
        return false;
    }

    std::swap(grid.at(coord.first).at(coord.second), grid.at(coord.first - 1).at(coord.second));
    return true;
}
