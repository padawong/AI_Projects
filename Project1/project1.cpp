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
Node* general_search(std::vector< std::vector<int> > &problem, std::string queueing_function) {
    std::pair<int, int> coord;
    std::vector< std::vector<int> > goal_state = {{1,2,3},{4,5,6},{7,8,0}};
    std::priority_queue<Node*> queue;
    std::vector<Node*> open_list;
    std::vector<Node*> closed_list;
    int expanded = 0;
    int queue_max = 0;
    
    // Populate initial queue
    // Each node is a state of the puzzle
    Node* initial_state = new Node(problem);
    queue.push(initial_state);
    open_list.push_back(initial_state);

    while(true) {
        // If queue is empty, return failure
        if (queue.empty()) {
            return nullptr;
        }

        Node* current = queue.top();
        queue.pop();

        // Goal state found
        if (current->grid == goal_state) {
            std::cout << "\nGoal!" << std::endl;
            std::cout << "The search algorithm expanded " << expanded << " nodes" << std::endl;
            std::cout << "The maximum number of nodes in the queue at any one time was: " << queue_max << std::endl;
            std::cout << "The depth of the goal node is: " << current->depth << std::endl;

            // std::cout << "Open list: "  << open_list.size() << std::endl;
            // std::cout << "Closed list: "  << closed_list.size() << std::endl;
            return current;
        }
        // Update open/closed lists to reflect imminent expansion of the current grid configuration
        else {
            int pos;
            Node* temp;
            pos = node_at(current, open_list);
            temp = open_list.at(pos);
            closed_list.push_back(temp);
            open_list.erase(open_list.begin() + pos);
        }

        // Expand current node and update queue and lists
        std::cout << "Currently expanding: " << std::endl;
        print_grid(current->grid);
        // std::cout << "Open list: "  << open_list.size() << std::endl;
        // std::cout << "Closed list: "  << closed_list.size() << std::endl;
        std::cout << "====================" << std::endl;
        expanded++;
        update_queue(current, queue, open_list, closed_list, queueing_function);

        // Update max queue size
        if (queue.size() > queue_max) {
            queue_max = queue.size();
        }
    }

}


/* UNIFORM COST QUEUEING FUNCTION
 * Performs all expansion and enqueueing for the node currently being examined
 * Checks to see if the grid configuration has been seen before or is currently in queue; if so, does not add
 */
void update_queue(Node* node, std::priority_queue<Node*> &queue, std::vector<Node*> &open_list, std::vector<Node*> &closed_list, std::string queueing_function) {
    int open_pos, closed_pos;
    std::vector<Node*> moves;
    Node* curr_node;

    std::pair<int, int> zero_loc = find_zero(node->grid);
    moves.push_back(move_right(node, zero_loc));
    moves.push_back(move_left(node, zero_loc));
    moves.push_back(move_up(node, zero_loc));
    moves.push_back(move_down(node, zero_loc));

    for (int i = 0; i < moves.size(); i++) {
        curr_node = moves.at(i);

        // Valid move
        if (curr_node != nullptr) {
            open_pos = node_at(curr_node, open_list);
            closed_pos = node_at(curr_node, closed_list);

            // No match found in either list
            // Push onto queue and add to open_list
            if (open_pos == -1 && closed_pos == -1) {
                std::vector<std::vector<int> > curr_grid = curr_node->grid;
                if (queueing_function == "Uniform Cost") {
                    // DO NOTHING
                    // queue.push(curr_node);
                }
                else if (queueing_function == "Misplaced Tile") {
                    // Checks all entries to count misplaced tiles
                    // Loop checks all but the final entry
                    for (int x = 1; x <= curr_grid.size(); x++) {
                        for (int y = 0; y < curr_grid.size() - 1; y++) {
                            // If value (other than max value) is not in the right place, increment heuristic
                            if (curr_grid.at(x).at(y) != x + y) {
                                curr_node->heuristic++;
                            }
                        }
                    }
                    // Check final entry for 0
                    if (curr_grid.at(curr_grid.size() - 1).at(curr_grid.size() - 1) != 0) {
                        curr_node->heuristic++;
                    }

                }
                else { // Manhattan Distance

                }
                // Enqueue (will automatically adjust for heuristics)
                queue.push(curr_node);

                open_list.push_back(curr_node);
            }
        }
    }
}

// Returns coordinates of the empty space in the grid
std::pair<int, int> const find_zero(std::vector<std::vector<int> > &grid) {
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid.size(); j++) {
            if (grid.at(i).at(j) == 0) {
                return std::make_pair(i, j);
            }
        }
    }
}

void const print_grid(std::vector< std::vector<int> > &grid) {
    for (int i = 0; i < grid.size(); i++) {
        for (int j = 0; j < grid.size(); j++) {
            std::cout << grid.at(i).at(j) << " ";
        }
        std::cout << std::endl;
    }
    std::cout << std::endl;

    return;
}

// Checks if a grid configuration is in a list
// If so, returns the position
int node_at(Node* node, std::vector<Node*> &list_in) {
    for (int i = 0; i < list_in.size(); i++) {
        if (node->grid == list_in.at(i)->grid) {
            return i;
        }
    }
    return -1;
}
