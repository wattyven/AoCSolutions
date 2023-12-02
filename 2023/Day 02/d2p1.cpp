#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

struct Game {
    int id;
    vector<map<string, int>> rounds;
};

vector<Game> readInput(const string& filename) {
    vector<Game> games;
    ifstream file(filename);
    string line;

    while (getline(file, line)) {
        stringstream ss(line);
        Game game;
        string token;

        getline(ss, token, ':');
        game.id = stoi(token.substr(5));

        while (getline(ss, token, ';')) {
            map<string, int> round;
            stringstream roundStream(token);
            string color;
            int count;

            while (roundStream >> count >> color) {
                color.erase(remove(color.begin(), color.end(), ','), color.end());

                round[color] = count;
            }

            game.rounds.push_back(round);
        }
        games.push_back(game);
    }
    return games;
}

bool gameValid(const Game& game, const map<string, int>& bag) {
    for (const auto& round : game.rounds) {
        for (const auto& cube : round) {
            if (bag.find(cube.first) == bag.end() || cube.second > bag.at(cube.first)) {
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        cerr << "Usage: " << argv[0] << " <inputfile>" << endl;
        return 1;
    }

    vector<Game> games = readInput(argv[1]);
    map<string, int> bag = {{"red", 12}, {"green", 13}, {"blue", 14}};
    int idsum = 0;

    for (const auto& game : games) {
        if (gameValid(game, bag)) {
            sumOfIds += game.id;
        }
    }

    cout << idsum << endl;
    return 0;
}
