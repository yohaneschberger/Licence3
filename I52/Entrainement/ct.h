#ifndef H_OUVRAGE
#define H_OUVRAGE

#include <string>
using namespace std;

class Ouvrage
{
    protected:
        string ISBN;
        string titre;
        string auteur;
    public:
        Ouvrage();
        Ouvrage(string,string,string);
        Ouvrage(const Ouvrage &);

        void Affic();
};

#endif