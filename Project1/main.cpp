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

    std::pair<int, int> coord;

    //print_grid(grid);
    Node* final_grid = uniform_cost(grid);
    print_grid(final_grid->grid);
    //coord = find_zero(grid);
    
    // std::cout << "Please entered desired dimensions: " << std::endl;
    // std::getline(std::cin, dim_in);
    // dimensions = stoi(dim_in);

    // grid = generate_grid(dimensions);


    return 0;
}
