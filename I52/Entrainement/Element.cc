#include <iostream>
#include <string>
using namespace std;

#include "ct.h"
#include "Element.h"

Element::Element()
{
    cote = 0;
    dispo = false;
}

Element::Element(int c)
{
    cote = c;
    dispo = true;
}

int Element::GetCote() const
{
    return cote;
}

bool Element::GetDispo() const
{
    return dispo;
}

void Element::ModDispo()
{
    if (dispo)
        dispo = false;
    else
        dispo = true;
}

ostream& operator<<(ostream & o, const Element & e)
{
    o << e.GetCote() << " | " << e.GetDispo() << endl;
    return o;
}