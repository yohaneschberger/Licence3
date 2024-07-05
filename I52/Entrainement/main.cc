#include <iostream>
using namespace std;

#include "ct.h"
#include "Element.h"

int main()
{
    Ouvrage O;
    Ouvrage livre("2-212-08985-6", "Programmer en langage C", "Claude Delannoy"); 
    Ouvrage livre2(livre);
    livre2.Affic();

    return 0;
}