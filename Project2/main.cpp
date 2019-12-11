#include <cstdlib>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

int main() {

    // All features stored in a 2D vector
    int

    /*
    for (int i = 0; i < line.size(); i++) {
        for (int j = 0; j < lines.size(); j++) {
    */

    std::ifstream file("CS170_SMALLtestdata_119.txt");
    std::string line;
    while (std::getline(file, line)) {
        std::istringstream line_in(line);



    double number = std::strtod("8.7986390e-03", NULL);
    std::cout.precision(8);
    std::cout << number << std::endl;

    return 0;

}
