#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    cout << "Nombre n°1: " << endl;

    int nombre1(0);
    cin >> nombre1;

    cout << "Nombre n°2: " << endl;
    int nombre2(0);
    cin >> nombre2;

    cout << nombre1 + nombre2 << endl;
    return 0;
}