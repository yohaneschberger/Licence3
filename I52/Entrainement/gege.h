#include <iostream>
using namespace std;

template <typename T>

class ElementGen {
private:
    T cote;
    bool dispo;

public:
    // Constructeur par défaut
    ElementGen() : dispo(true) {}

    // Constructeur avec un seul argument pour définir cote et mettant dispo à vrai
    ElementGen(T coteValue) : cote(coteValue), dispo(true) {}

    // Accesseur GetCote
    T GetCote() const { return cote; }

    // Accesseur GetDispo
    bool GetDispo() const { return dispo; }

    // Modificateur ModDispo
    void ModDispo(bool newDispo) { dispo = newDispo; }

    // Fonction membre Affic pour l'affichage
    void Affic() const {
        cout << "Cote: " << cote << ", Disponible: " << (dispo ? "Oui" : "Non") << endl;
    }
};