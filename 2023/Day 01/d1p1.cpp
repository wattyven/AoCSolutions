#include <iostream>
#include <fstream>
#include <string>
#include <cctype>

int main(int argc, char *argv[]) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " <filename>\n";
        return 1;
    }
    std::ifstream file(argv[1]);
    if (!file) {
        std::cerr << "Error opening file: " << argv[1] << "\n";
        return 1;
    }
    std::string line;
    int sum = 0;

    while (std::getline(file, line)) {
        int first = -1, last = -1;
        for (char c : line) {
            if (std::isdigit(c)) {
                first = c - '0';
                break;
            }
        }
        for (auto it = line.rbegin(); it != line.rend(); ++it) {
            if (std::isdigit(*it)) {
                last = *it - '0';
                break;
            }
        }
        if (first != -1 && last != -1) {
            sum += first * 10 + last;
        }
    }

    std::cout << sum << std::endl;
    return 0;
}
