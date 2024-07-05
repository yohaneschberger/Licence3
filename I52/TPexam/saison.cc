#include <iostream>
#include <string>
using namespace std;

#include "saison.h"

Saison::Saison()
{
    nbEpisodes = 0;
    liste = NULL;
}

Saison::Saison(int nb)
{
    nbEpisodes = nb;
    liste = new Episode [nbEpisodes];
    for(int i = 0; i < nbEpisodes; i++)
        liste[i] = Episode();
}

Saison::Saison(int nb, Episode* e)
{
    nbEpisodes = nb;
    liste = new Episode [nbEpisodes];
    for(int i = 0; i < nbEpisodes; i++)
        liste[i] = e[i];
}

Saison::Saison(const Saison & s)
{
    nbEpisodes = s.nbEpisodes;
    liste = new Episode [nbEpisodes];
    for(int i = 0; i < nbEpisodes; i++)
        liste[i] = s.liste[i];
}


//Destructeur

Saison::~Saison()
{
    delete [] liste;
}

Saison& Saison::operator=(const Saison & s)
{
    if(this != &s)
    {
        nbEpisodes = s.nbEpisodes;
        delete [] liste;
        liste = new Episode [nbEpisodes];
        for(int i = 0; i < nbEpisodes; i++)
            liste[i] = s.liste[i];
    }
    return *this;
}

Saison Saison::operator+(const Episode & e)const
{
    Saison res(nbEpisodes + 1);
    for(int i = 0; i < nbEpisodes; i++)
        res[i] = liste[i];
    res[nbEpisodes] = e;
    return res;
}

