#include "project1.h"

/* Algorithm:
 * nodes = make_queue(initial_state)
 * loop do
 *      if empthy(nodes) return failure
 * node = remove_front(node)
 * if goal state
 *      return node
 * node = queueing function(nodes, expand(node))
 *
 * Each node is a state of the puzzle
 * For Uniform Length, queueing/dequeueing is basically BFS
 *
 * Will need to create a node class to hold heuristic value
 */
void uniform_cost(std::vector< std::vector<int> > grid) {
    std::pair<int, int> coord;
    std::vector< std::vector<int> > goal_state = {{1,2,3},{4,5,6},{7,8,0}};

    coord = find_zero(grid);

    // Make queue
    // Each node is a state of the puzzle
    
    

}

std::pair<int, int> const find_zero(std::vector<std::vector<int> > &grid) {
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid.size(); j++) {
            if (grid.at(i).at(j) == 0) {
                return std::make_pair(i, j);
            }
        }
    }
}

void print_grid(std::vector< std::vector<int> > grid) {

    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid.size(); j++) {
            std::cout << grid.at(i).at(j) << " ";
        }
        std::cout << std::endl;
    }

    return;
}
