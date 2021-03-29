#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int lightX; // the X position of the light of power
    int lightY; // the Y position of the light of power
    int initialTX; // Thor's starting X position
    int initialTY; // Thor's starting Y position
    cin >> lightX >> lightY >> initialTX >> initialTY; cin.ignore();
    string solution;

    // game loop
    while (1) {
        int remainingTurns; // The remaining amount of turns Thor can move. Do not remove this line.
        cin >> remainingTurns; cin.ignore();
        solution = "";

        if (initialTY < lightY) {
            solution += "S";
            initialTY += 1;
        }

        else if (initialTY > lightY) {
            solution += "N";
            initialTY -= 1;
        }

        if (initialTX < lightX) {
            solution += "E";
            initialTX += 1;
        }

        else if (initialTX > lightX) {
            solution += "W";
            initialTX -= 1;
        }

        // A single line providing the move to be made: N NE E SE S SW W or NW
        cout << solution << endl;
    }
}