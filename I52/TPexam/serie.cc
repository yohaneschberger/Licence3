#include <iostream>
#include <string>
using namespace std;

#include "serie.h"

Serie::Serie()
{
    titreSerie = "";
	comedie = false;
	genre = "";
	nbSaison = 0;
	enPublic = false;
}

Serie::Serie(string t, bool c, string g, int nb, bool p)
{
    titreSerie = t;
	comedie = c;
	genre = g;
	nbSaison = nb;
	enPublic = p;
}

Serie::Serie(const Serie & s)
{
    titreSerie = s.titreSerie;
	comedie = s.comedie;
	genre = s.genre;
	nbSaison = s.nbSaison;
	enPublic = s.enPublic;
}

string Serie::Get_titreSerie() const
{
    return titreSerie;
}

int Serie::Get_nbSaison() const
{
    return nbSaison;
}

bool Serie::shortcom()
{
    return comedie && !enPublic;
}

bool Serie::sitcom()
{
    return comedie && enPublic;
}

void Serie::affiche()
{
    cout << titreSerie << endl;
    cout << (sitcom()?"sitcom":(shortcom()?"shortcom":"Ce n'est ni un shortcom ni un sitcom")) << endl;
    cout << genre << endl;
    cout << nbSaison; 
}