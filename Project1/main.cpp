#include "project1.h"

int main () {
    std::string dim_in;
    int dimensions;
    std::vector< std::vector<int> > grid, trivial, very_easy, easy, doable, oh_boy, impossible;
    std::pair<int, int> coord;
    std::string input, nums_in, queueing_function;

    trivial.push_back({1, 2, 3});
    trivial.push_back({4, 5, 6});
    trivial.push_back({7, 8, 0});

    very_easy.push_back({1, 2, 3});
    very_easy.push_back({4, 5, 6});
    very_easy.push_back({7, 0, 8});

    easy.push_back({1, 2, 0});
    easy.push_back({4, 5, 3});
    easy.push_back({7, 8, 6});

    doable.push_back({0, 1, 2});
    doable.push_back({4, 5, 3});
    doable.push_back({7, 8, 6});

    oh_boy.push_back({8, 7, 1});
    oh_boy.push_back({6, 0, 2});
    oh_boy.push_back({5, 4, 3});

    impossible.push_back({1, 2, 3});
    impossible.push_back({4, 5, 6});
    impossible.push_back({8, 7, 0});

//    do {
    std::cout << "Welcome to Erin Wong's 8-puzzle solver!" << std::endl;

    do {
        std::cout << "Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle." << std::endl;
        std::getline(std::cin, input);
    } while (input != "1" && input != "2");

    // Default puzzle
    if (input == "1") {
        do {
            std::cout << "Please select a difficulty level: " << std::endl;
            std::cout << "1. Trivial" << std::endl;
            std::cout << "2. Very Easy" << std::endl;
            std::cout << "3. Easy" << std::endl;
            std::cout << "4. Doable" << std::endl;
            std::cout << "5. Oh Boy" << std::endl;
            std::cout << "6. Impossible" << std::endl;
            std::getline(std::cin, nums_in);
        } while (nums_in != "1" && nums_in != "2" && nums_in != "3" && nums_in != "4" && nums_in != "5" && nums_in != "6");

        if (nums_in == "1") {
            grid = trivial;
        }
        else if (nums_in == "2") {
            grid = very_easy;
        }
        else if (nums_in == "3") {
            grid = easy;
        }
        else if (nums_in == "4") {
            grid = doable;
        }
        else if (nums_in == "5") {
            grid = oh_boy;
        }
        else if (nums_in == "6") {
            grid = impossible;
        }
    }

    // Custom puzzle
    if (input == "2") {
        std::cout << "Enter your puzzle using a 0 to represent the blank" << std::endl;
        for (int i = 0; i < 3 ; i++) {
            std::vector<int> row;
            std::cout << "Enter the " << i << "th row. Use space or newline between numbers" << std::endl;
            for (int j = 0; j < 3 ; j++) {
                std::getline(std::cin, nums_in);
                row.push_back(std::stoi(nums_in));
                nums_in.clear();
            }
            grid.push_back(row);
        }
    }

    std::cout << "The puzzle is as follows: " << std::endl;
    print_grid(grid);

    do {
        std::cout << "Enter your choice of algorithm: " << std::endl;
        std::cout << "1. Uniform Cost Search" << std::endl;
        std::cout << "2. A* with the Misplaced Tile heuristic" << std::endl;
        std::cout << "3. A* with the Manhattan distance heuristic" << std::endl;

        std::getline(std::cin, input);
    } while (input != "1" && input != "2" && input != "3");

    if (input == "1") {
        queueing_function = "Uniform Cost";
    }
    else if (input == "2") {
        queueing_function = "Misplaced Tile";
    }
    else {
        queueing_function = "Manhattan Distance";
    }

    std::cout << "SOLVER BEGINNING. Expanding state: " << std::endl;
    print_grid(grid);

    //Node final_grid = general_search(grid, "Uniform Cost");
    Node final_grid = general_search(grid, queueing_function);
    print_grid(final_grid.grid);

    return 0;
}
