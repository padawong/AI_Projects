#include <cstdlib>
#include <string>
#include <iostream>

int main() {

    /*
    for (int i = 0; i < line.size(); i++) {
        for (int j = 0; j < lines.size(); j++) {
    */

    double number = std::strtod("8.7986390e-03", NULL);
    std::cout.precision(8);
    std::cout << number << std::endl;

    return 0;

}
