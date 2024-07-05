#include <iostream>
#include <string>
using namespace std;

#include "episode.h"

Episode::Episode()
{
    titreEpisode = "";
	numEpisode = 0;
	numSaison = 0;
	duree = 0.0;
}

Episode::Episode(string t, bool c, string g, int nb, bool p, string tepi, int nepi, int nsai, float d):Serie(t,c,g,nb,p)
{
    titreEpisode = tepi;
    numEpisode = nepi;
    numSaison = nsai;
    duree = d;
}

Episode::Episode(const Episode & e):Serie(e)
{
    titreEpisode = e.titreEpisode;
    numEpisode = e.numEpisode;
    numSaison = e.numSaison;
    duree = e.duree;
}

bool Episode::shortcom()
{
    bool res = Serie::shortcom();
    return res && (duree < 10);
}

bool Episode::sitcom()
{
    bool res = Serie::sitcom();
    return res && (duree < 30);
}

ostream& operator<<(ostream& o, const Episode & e)
{
    o << e.Get_titreSerie() << " | " << e.numSaison << " | " << e.numEpisode << " | " << e.titreEpisode;
    return o;
}