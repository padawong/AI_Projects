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
Node* uniform_cost(std::vector< std::vector<int> > &grid) {
    std::pair<int, int> coord;
    std::vector< std::vector<int> > goal_state = {{1,2,3},{4,5,6},{7,8,0}};
    std::queue<Node*> queue;
    std::vector<Node*> open_list;
    std::vector<Node*> closed_list;
    int expanded = 0;
    int queue_max = 0;
    
    // Populate initial queue
    // Each node is a state of the puzzle
    Node* initial_state = new Node(grid);
    queue.push(initial_state);
    open_list.push_back(initial_state);

    while(true) {
        // If queue is empty, return failure
        if (queue.empty()) {
            return nullptr;
        }

        Node* current = queue.front();
        queue.pop();

        // Goal state found
        if (current->grid == goal_state) {
            std::cout << "Goal!" << std::endl;
            std::cout << "The search algorithm expanded " << expanded << " nodes" << std::endl;
            std::cout << "The maximum number of nodes in the queue at any one time was: " << queue_max << std::endl;
            std::cout << "The depth of the goal node is: " << current->depth << std::endl;
            return current;
        }

        // Expand current node and update queue and lists
        std::cout << "Currently expanding: " << std::endl;
        print_grid(current->grid);
        std::cout << "====================" << std::endl;
        expanded++;
        update_queue(current, queue, open_list, closed_list);
        if (queue.size() > queue_max) {
            queue_max = queue.size();
        }
    }

}

void update_queue(Node* node, std::queue<Node*> &queue, std::vector<Node*> &open_list, std::vector<Node*> &closed_list) {
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
                curr_node->depth++;
                queue.push(curr_node);
                //print_grid(curr_node->grid);
                open_list.push_back(curr_node);
            }
        }
    }
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

int node_at(Node* node, std::vector<Node*> &list_in) {
    for (int i = 0; i < list_in.size(); i++) {
        i (node->grid == list_in.at(i)->grid) {
            return i;
        }
    }
    return -1;
}
