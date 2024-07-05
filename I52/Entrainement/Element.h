#ifndef H_ELEMENT
#define H_ELEMENT

#include "ct.h"
#include <iostream>
using namespace std;

class Element : public Ouvrage
{
    private:
        int cote;
        bool dispo;
    public:
        Element();
        Element(int);

        int GetCote() const;
        bool GetDispo() const;

        void ModDispo();

        friend ostream& operator<<(ostream &, const Element &);
};

#endif