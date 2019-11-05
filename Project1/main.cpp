#include "project1.h"

int main () {
    std::string dim_in;
    int dimensions;
    std::vector< std::vector<int> > grid;
    // grid.push_back({1, 2, 4});
    // grid.push_back({3, 8, 6});
    // grid.push_back({7, 0, 5});
    grid.push_back({0, 1, 2});
    grid.push_back({4, 5, 3});
    grid.push_back({7, 8, 6});
    // grid.push_back({1, 2, 0});
    // grid.push_back({4, 5, 3});
    // grid.push_back({7, 8, 6});

    std::pair<int, int> coord;

    //Node* final_grid = general_search(grid, "Uniform Cost");
    Node* final_grid = general_search(grid, "Misplaced Tile");
    print_grid(final_grid->grid);

    return 0;
}
