#include <stdio.h>
#include <stdlib.h>

// EXERCICE 1

typedef unsigned char VECTEUR;

// 1.2
/*int pow2(unsigned int n)
{
    return 1 << n;
}*/

// 1.3
/*VECTEUR vecteur_vide()
{
    return 0;
}*/

// 1.4
void affiche_vecteur(VECTEUR v, unsigned int n)
{
    int i;
    for(i = n-1; i >= 0; i--)
    {
        printf("%d ", (v >> i) & 1);
    }
}

// EXERCICE 2


// 2.1
VECTEUR* mots(unsigned int k)
{
    if(k <= 0) return NULL;
    
    VECTEUR* vecteurs = (VECTEUR*)malloc((1 << k) * sizeof(VECTEUR));
    unsigned int i;
    for(i = 0; i < (1 << k); i++)
    {
        vecteurs[i] = i;
    }
    return vecteurs;
}

// 2.2
int poids(VECTEUR v, int n)
{
    int p = 0;
    for(int i = 0; i < n; i++)
    {
        if ((v >> i) & 1) p++;
    }
    return p;
}

// 2.3
/*VECTEUR diff(VECTEUR u, VECTEUR v)
{
    if((u == 0) && (v == 0)) return 0;

    return u ^ v;
}*/

// 2.4
unsigned int hamming(VECTEUR u, VECTEUR v, int n)
{
    if((u == 0) && (v == 0)) return 0;
    return poids(u^v, n);
}

// EXERCICE 3

typedef VECTEUR* MATRICE;

// 3.2
void affiche_matrice(MATRICE mat, unsigned int l, unsigned int c, unsigned int order)
{
    unsigned int i;
    if (order == 0)
    {
        for(i = 0; i < l; i++)
        {
            affiche_vecteur(mat[i], c);
            printf("\n");
        }
        return;
    }
    for(i = 0; i < c; i++)
    {
        for(unsigned int j = 0; j < l; j++)
        {
            printf("%d ", (mat[j] >> i) & 1);
        }
    printf("\n");
    }
}


// 3.3
VECTEUR encode(MATRICE g, VECTEUR v, unsigned int k, unsigned int n)
{
    VECTEUR r = 0;
    unsigned int i, j;
    for(i = 0; i < k; i++)  // Pour chaque ligne de la matrice
    {
        for(j = 0; j < n; j++)  // Pour chaque colonne de la matrice
        {
            r ^= ((v >> i) & 1) * ((g[i] >> j) & 1) << j;   // On effectue le produit scalaire entre la i-ème ligne de la matrice et le vecteur v
        }
    }
    return r;
}

// 3.5
unsigned int dist_min(VECTEUR* vecteurs, unsigned int n, unsigned int nbVecteurs)
{
    if(nbVecteurs <= 1)
    {
        return 0;
    }
    
    unsigned int d = n;
    unsigned int i, j;
    for(i = 0; i < nbVecteurs; i++)
    {
        for(j = i + 1; j < nbVecteurs; j++)
        {
            unsigned int h = hamming(vecteurs[i], vecteurs[j], n);
            if(h < d) d = h;
        }
    }
    return d;
}

// EXERCICE 4

typedef unsigned char SYNDROME;

// 4.2
SYNDROME syndrome(MATRICE h, VECTEUR c, unsigned int k, unsigned int n)
{
    SYNDROME s = 0;
    for(int i = 0; i < n-k; i++)  // Pour chaque ligne de la matrice
    {
        for(int j = 0; j < n; j++)  // Pour chaque colonne de la matrice
        {
            s ^= ((c >> j) & 1) * ((h[i] >> j) & 1) << i;   // On effectue le produit scalaire entre la i-ème colonne de la matrice et le vecteur c
        }
    }
    return s;
}

// EXERCICE 5

// 5.1
VECTEUR bruite(VECTEUR v, unsigned int b)
{
    return v ^= 1UL << b;   // L'expression 1UL << b crée un masque avec un 1 au bit b et des 0 partout ailleurs
}

// EXERCICE 6


// 6.2
int indice_colonne(SYNDROME s, MATRICE h, unsigned int k, unsigned int n)
{
    if(s == 0 || h == NULL) return -1;

    for(unsigned int i = 0; i < n; i++)
    {
        SYNDROME col = 0;
        for(unsigned int j = 0; j < n-k; j++)
        {
            col |= ((h[j] >> i) & 1) << j;
        }
        if(col == s) return i;
    }
    return -1;
}

// 6.3
VECTEUR corrige(VECTEUR v, MATRICE h, unsigned int k, unsigned int n)
{
    SYNDROME s = syndrome(h, v, k, n);
    int indice = indice_colonne(s, h, k, n);
    if (indice == -1) return v;
    return bruite(v, indice);
}

// 6.4
VECTEUR decode(VECTEUR v, unsigned int k, unsigned int n)
{
    VECTEUR masque = (1 << (n - k)) - 1;
    v &= masque;
    return v;
}

int main()
{
    // EXERCICE 1
    printf("EXERCICE 1\n");

    // 1.3
    VECTEUR v = 0;

    // 1.4
    affiche_vecteur(v, 8);
    printf("\n");
    affiche_vecteur(16, 8);
    printf("\n");

    // 1.5 Vu que VECTEUR est un unsigned char, si on met une valeur entière (inférieure à 256), cela retournera la valeur en binaire.

    // 1.6 De base, on donne des valeurs décimales

    // EXERCICE 2
    printf("\nEXERCICE 2\n");

    // 2.1
    VECTEUR* tab = mots(3);
    for (int i = 0; i < 8; i++)
    {
        affiche_vecteur(tab[i], 3);
        printf("\n");
    }

    // 2.2
    printf("\n");
    printf("Poids de 5: %d\n", poids(5, 8));

    // 2.3
    printf("Différence entre 5 et 3: ");
    affiche_vecteur(5^3, 8);
    printf("\n");

    // 2.4
    printf("Distance de Hamming entre 5 et 3: %d\n", hamming(5, 3, 8));

    // EXERCICE 3
    printf("\nEXERCICE 3\n");

    // Définir la matrice G
    MATRICE G = malloc(4 * sizeof(VECTEUR));
    G[0] = 81;
    G[1] = 114;
    G[2] = 52;
    G[3] = 104;

    // 3.2
    // Afficher la matrice G
    printf("Matrice G (order = 0):\n");
    affiche_matrice(G, 4, 7, 0);
    printf("\n");
    printf("Matrice G (order = 1):\n");
    affiche_matrice(G, 4, 7, 1);

    printf("\n");

    // 3.3
    // Générer tous les vecteurs de taille 4
    VECTEUR* vecteurs = mots(4);
    if (vecteurs == NULL)
    {
        printf("Erreur d'allocation de mémoire\n");
        return 1;
    }

    // Encoder chaque vecteur avec la matrice G
    VECTEUR* mots_codes = malloc((1 << 4) * sizeof(VECTEUR));
    if (mots_codes == NULL)
    {
        printf("Erreur d'allocation de mémoire\n");
        return 1;
    }

    printf("Vecteur non encodé\nVecteur encodé\n\n");

    for (int i = 0; i < (1 << 4); i++)
    {
        // Afficher le vecteur non encodé
        affiche_vecteur(vecteurs[i], 4);
        printf(" \n");

        // Encoder le vecteur
        mots_codes[i] = encode(G, vecteurs[i], 4, 7);

        // Afficher le vecteur encodé
        affiche_vecteur(mots_codes[i], 7);

        // Ajouter une ligne vide pour séparer les paires de vecteurs
        printf("\n\n");
    }

    // 3.5
    printf("Distance minimale: %d\n", dist_min(vecteurs, 4, 1 << 4));

    // 3.6
    printf("Capacité de décodage: %d\n", (dist_min(vecteurs, 4, 1 << 4) - 1) / 2);

    // EXERCICE 4
    printf("\nEXERCICE 4\n");

    // Définir la matrice H
    MATRICE H = malloc(8 * sizeof(VECTEUR));
    H[0] = 23;
    H[1] = 46;
    H[2] = 75;

    affiche_matrice(H, 3, 7, 0);

    // 4.3
    // On peut déduire de l'étude des syndromes par rapport aux mots du code que lorsque le syndrome est nul, le mot du code est correct.

    // EXERCICE 5
    printf("\nEXERCICE 5\n");

    // 5.1
    printf("<vecteur normal> - <syndrome original> - <vecteur bruité> - <syndrome bruité>\n");

    // On définit les vecteurs à tester
    VECTEUR vecteur[] = {0, 114, 52, 70, 23, 57, 13};

    // On définit les indices à bruité
    int indices[] = {0, 1, 2, 3, 4, 5, 6};

    for (int i = 0; i < 7; i++)
    {
        SYNDROME s_orig = syndrome(H, vecteur[i], 4, 7);
        VECTEUR v_bruit = bruite(vecteur[i], indices[i]);
        SYNDROME s_bruit = syndrome(H, v_bruit, 4, 7);

        // Afficher le vecteur original, le syndrome original, le vecteur bruité et le syndrome bruité
        printf("< ");
        affiche_vecteur(vecteur[i], 7);
        printf("> - < ");
        affiche_vecteur(s_orig, 3);
        printf("> - < ");
        affiche_vecteur(v_bruit, 7);
        printf("> - < ");
        affiche_vecteur(s_bruit, 3);
        printf(">\n");

        VECTEUR v_corrige = corrige(v_bruit, H, 4, 7);
        printf("Corrige : < ");
        affiche_vecteur(v_corrige, 7);
        printf(">\n");

        VECTEUR v_decode = decode(v_corrige, 4, 7);
        printf("Decode : < ");
        affiche_vecteur(v_decode, 4);
        printf(">\n\n");
    }

    // 5.1
    // chaque syndrome correspond à une colonne unique de H.
    // Cette correspondance permet d'identifier la position du bit erroné dans le vecteur transmis.

    // EXERCICE 6
    printf("\nEXERCICE 6\n");

    // 6.2

    // Définir les syndromes à tester
    SYNDROME syndromes[] = {5, 7, 3, 6, 1, 2, 4};

    // Parcourir les syndromes
    for (int i = 0; i < 7; i++)
    {
        int indice = indice_colonne(syndromes[i], H, 4, 7);
        printf("Syndrome: %d, Indice de colonne: %d\n", syndromes[i], indice);
    }

    // 6.1 A mon avis, les fonctions pow2, vecteur_vide et diff ne sont pas nécessaires car on travaille directement avec des opérations binaires.

    // 6.2 Chaque colonne est une permutation circulaire de la première colonne. H2 est une matrice de contrôle cyclique.
    // Une matrice de contrôle cyclique permet de simplifier le calcul des syndromes et de corriger les erreurs.
    // Pour calculer le syndrome, il suffit de faire le produit matriciel entre le vecteur reçu et la première colonne de la matrice de contrôle,
    // puis de faire des rotations circulaires de ce résultat pour obtenir les autres éléments du syndrome.

    // Libérer la mémoire
    free(vecteurs);
    free(mots_codes);   
    free(G);
    free(H);
    free(tab);

    return 0;
}

