#include "project1.h"

/* Follows Provided Algorithm
 *
 * Each node is a state of the puzzle
 * Makes queue from initial state
 * Loop:
 *   if queue is empty, return failure
 *   else equeue node
 *   if node is goal state, return node
 *   else expand node by sending to queueing_function 
 */
Node general_search(std::vector< std::vector<int> > &problem, std::string queueing_function) {
    std::pair<int, int> coord;
    std::vector< std::vector<int> > goal_state = {{1,2,3},{4,5,6},{7,8,0}};
    std::priority_queue<Node> queue;
    std::vector<Node*> open_list, closed_list;
    int expanded = 0;
    int queue_max = 0;
    
    // Populate initial queue
    // Each node is a state of the puzzle
    Node* initial_state = new Node(problem);
    queue.push(*initial_state);
    open_list.push_back(initial_state);

    while(true) {
        // If queue is empty, return failure
        if (queue.size() == 0) {
            std::cout << "FAILURE!" << std::endl;
            std::vector<std::vector<int> > failure = {{0,0,0}, {0,0,0}, {0,0,0}};
            Node failed(failure);
            delete initial_state;
            return failed;
        }
        Node curr = queue.top();
        queue.pop();

        Node* current = &curr;

        // Goal state found
        if (current->grid == goal_state) {
            std::cout << "Goal!" << std::endl;
            std::cout << "The search algorithm expanded " << expanded << " nodes" << std::endl;
            std::cout << "The maximum number of nodes in the queue at any one time was: " << queue_max << std::endl;
            std::cout << "The depth of the goal node is: " << current->depth << std::endl;
            delete initial_state;
            return *current;
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
        if (expanded < 1000 || expanded % 1000 == 0) {
            std::cout << "The best state to expand with a g(n) = " << current->depth << " and h(n) = " << current->heuristic << " is: " << std::endl;
            print_grid(current->grid);

            if (expanded >= 1000) {
                std::cout << "Expanded = " << expanded << std::endl;
            }

            std::cout << "Expanding this node..." << std::endl;
            // std::cout << "Open list: "  << open_list.size() << std::endl;
            // std::cout << "Closed list: "  << closed_list.size() << std::endl;
            std::cout << "====================\n" << std::endl;
        }

        // Expand node and update value
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
void update_queue(Node* node, std::priority_queue<Node> &queue, std::vector<Node*> &open_list, std::vector<Node*> &closed_list, std::string queueing_function) {
    int open_pos, closed_pos;
    std::vector<Node*> moves;
    Node* curr_node;
    //Node* parent_node = new Node(node);

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
                // UNIFORM COST
                if (queueing_function == "Uniform Cost") {
                    // DO NOTHING; No heuristic to update
                }
                
                // A* MISPLACED TILE
                // Checks all entries to count misplaced tiles
                // If value (other than correct empty slot) is not in the right place, increment heuristic
                else if (queueing_function == "Misplaced Tile") {
                    int correct_val = 1;
                    for (int x = 0; x < curr_grid.size(); x++) {
                        for (int y = 0; y < curr_grid.size(); y++) {
                            if (!(x == curr_grid.size() - 1 && y == curr_grid.size() - 1) && curr_grid.at(x).at(y) != correct_val) {
                                curr_node->heuristic++;
                            }
                            correct_val++;
                        }
                    }
                }

                // A* MANHATTAN DISTANCE
                // For each element in the grid (except 0), calculate the Manhattan distance
                // Manhattan distance = abs(x_expected - x_actual) + abs(y_expected - y_actual)
                else { 
                    int x_expected, y_expected;
                    int current_val;
                    int distance;
                    
                    for (int x = 0; x < curr_grid.size(); x++) {
                        for (int y = 0; y < curr_grid.size(); y++) {
                            current_val = curr_grid.at(x).at(y);

                            if (current_val == 0) {
                                continue;
                            }

                            x_expected = (current_val - 1) / curr_grid.size();
                            y_expected = (current_val - 1) % curr_grid.size();
                            distance = abs(x_expected - x) + abs(y_expected - y);
                            curr_node->heuristic += distance;
                            
                            // Restart search of entire grid
                            distance = 0;
                            current_val++;
                        }
                    }
                }

                // Enqueue (will automatically adjust for heuristics)
                Node temp = *curr_node;
                queue.push(temp);
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
