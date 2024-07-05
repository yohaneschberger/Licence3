#include <iostream>
#include <string>
using namespace std;

#include "ct.h"

Ouvrage::Ouvrage()
{
    ISBN = "";
    titre = "";
    auteur = "";
}

Ouvrage::Ouvrage(string code, string t, string a)
{
    ISBN = code;
    titre = t;
    auteur = a;
}

Ouvrage::Ouvrage(const Ouvrage & o)
{
    ISBN = o.ISBN;
    titre = o.titre;
    auteur = o.auteur;
}

void Ouvrage::Affic()
{
    cout << ISBN << " | " << titre << " | " << auteur << endl;
}