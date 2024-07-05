#include <stdio.h>
#include <stdlib.h>

// EXERCICE 1

typedef int* VECTEUR;

int pow2(unsigned int n)
{
  return 1 << n;
}

VECTEUR vecteur_vide(unsigned int n)
{
  VECTEUR v = (VECTEUR)calloc(n, sizeof(int));
  return v;
}

void affiche_vecteur(VECTEUR v, unsigned int n)
{
  printf("[ ");
  for(int i = 0; i < n-1; i++)
  {
    printf("%d, ", v[i]);
  }
  printf("%d ]\n", v[n-1]);
}

VECTEUR vecteur(unsigned int n, unsigned int valeur)
{
  if(pow2(n)>valeur)
  {
    VECTEUR res = vecteur_vide(n);
    for(int i = 0; i < n; i++)
    {
      res[i] = valeur & 1;
      valeur = valeur >> 1;
    }
    return res;
  }
  return NULL;
}

int valeur(VECTEUR v, unsigned int n)
{
  int res = 0;

  if(v == NULL)
  {
    return -1;
  }
  for(int i=0; i < n; i++)
  {
    if(v[i]==1)
    {
      res += pow2(i);
    }
  }
  return res;
}

// EXERCICE 2

VECTEUR* mots(unsigned int k)
{
  if(k>0)
  {
    VECTEUR* res = (VECTEUR*)calloc(pow2(k), sizeof(VECTEUR));
    for(int i = 0; i < pow2(k); i++)
    {
      res[i] = vecteur(k, i);
    }
    return res;
  }
  return NULL;
}

void affiche_vecteurv(VECTEUR* v, unsigned int k)
{
  printf("[ ");
  for(int i = 0; i < pow2(k); i++)
  {
    for(int j = 0; j < k; j++)
    {
      printf("%d ", v[i][j]);
    }
    printf(", ");
  }
  printf("]\n");
}

unsigned int poids(VECTEUR v, int n)
{
  unsigned int res = 0;

  if(v == NULL)
  {
    return 0;
  }
  for(int i = 0; i < n; i++)
  {
    if(v[i] == 1)
    {
      res++;
    }
  }
  return res;
}

VECTEUR diff(VECTEUR u, VECTEUR v, int n)
{
  if(u == NULL || v == NULL)
  {
    return NULL;
  }
  VECTEUR d = vecteur_vide(n);
  for(int i = 0; i < n; i++)
  {
    d[i] = u[i]^v[i];
  }
  return d;
}

unsigned int hamming(VECTEUR u, VECTEUR v, int n)
{
  if(u == NULL || v == NULL)
  {
    return 0;
  }
  VECTEUR d = diff(u, v, n);
  unsigned int res = poids(d, n);
  return res;
}

// EXERCICE 3

typedef int** MATRICE;

void affiche_matrice(MATRICE mat, unsigned int l, unsigned int c)
{
    for(int i=0; i < l; i++)
    {
        printf("[ ");
        for(int j=0; j < c; j++)
        {
            printf("%d ", mat[i][j]); // Ajout d'un espace après chaque élément
        }
        printf("]\n"); // Ajout d'un saut de ligne après chaque ligne
    }
}

VECTEUR encode(MATRICE g, VECTEUR v, unsigned int k, unsigned int n)
{
  VECTEUR c = vecteur_vide(n);
  for(int i=0; i < k; i++)
    for(int j=0; j < n; j++)
    {
      c[j] = c[j]^ (v[i] * g[i][j]);
    }
  return c;
}

unsigned int dist_min(VECTEUR* vecteurs, unsigned int n, unsigned int nb_vect)
{
    if(vecteurs == NULL || nb_vect < 2)
    {
        return 0;
    }

    unsigned int min_dist = n; // Initialiser à la taille maximale possible

    // Comparer chaque paire de vecteurs
    for (unsigned int i = 0; i < nb_vect - 1; i++)
    {
        for (unsigned int j = i + 1; j < nb_vect; j++)
        {
            // Calculer la distance de Hamming entre vecteurs[i] et vecteurs[j]
            unsigned int dist = 0;
            for (unsigned int k = 0; k < n; k++)
            {
                if (vecteurs[i][k] != vecteurs[j][k])
                {
                    dist++;
                }
            }
            if (dist < min_dist)
            {
                min_dist = dist;
            }
        }
    }
    return min_dist;
}

// EXERCICE 4

typedef int* SYNDROME;

SYNDROME syndrome(MATRICE h, VECTEUR c, unsigned int k, unsigned int n)
{
    // Créer un nouveau vecteur pour le syndrome
    SYNDROME s = (SYNDROME)malloc((n - k) * sizeof(int));
    if (s == NULL) {
        fprintf(stderr, "Erreur d'allocation de mémoire\n");
        exit(EXIT_FAILURE);
    }

    // Calculer le syndrome
    for (unsigned int i = 0; i < n - k; i++)
    {
        s[i] = 0;
        for (unsigned int j = 0; j < n; j++)
        {
            s[i] += c[j] * h[i][j];
        }
        // Calculer le modulo 2 du résultat
        s[i] %= 2;
    }
    return s;
}

// EXERCICE 5

VECTEUR bruite(VECTEUR v, unsigned int n, unsigned int b)

{
    // Vérifier si le vecteur est nul ou si l'indice est invalide
    if (v == NULL || b >= n) {
        return NULL;
    }

    // Allouer de la mémoire pour le nouveau vecteur
    VECTEUR v_bruite = (VECTEUR)malloc(n * sizeof(int));
    if (v_bruite == NULL) {
        fprintf(stderr, "Erreur d'allocation de mémoire\n");
        exit(EXIT_FAILURE);
    }

    // Copier le vecteur et inverser le bit à l'indice b
    for (unsigned int i = 0; i < n; i++) {
        if (i == b) {
            v_bruite[i] = 1 - v[i]; // Inverser le bit
        } else {
            v_bruite[i] = v[i]; // Copier le bit
        }
    }
    return v_bruite;
}

int indice_colonne(SYNDROME s, MATRICE h, unsigned int k, unsigned int n) {
    // Vérifier si le syndrome ou la matrice est nul
    if (s == NULL || h == NULL) {
        return -1;
    }
    // Parcourir chaque colonne de la matrice
    for (unsigned int j = 0; j < n; j++) {
        int correspond = 1; // Indicateur de correspondance
        // Parcourir chaque élément de la colonne
        unsigned int i;
        for (i = 0; i < n - k && correspond; i++) {
            if (s[i] != h[i][j]) {
                correspond = 0; // Pas de correspondance
            }
        }
        if (correspond) {
            return j;
        }
    }
    return -1;
}

VECTEUR corrige(VECTEUR v, MATRICE h, unsigned int k, unsigned int n) {
    // Calculer le syndrome du vecteur v
    SYNDROME s = syndrome(h, v, k, n);
    // Trouver l'indice de la colonne de h qui correspond au syndrome
    int indice = indice_colonne(s, h, k, n);
    // Allouer de la mémoire pour le vecteur corrigé
    VECTEUR v_corrige = (VECTEUR)malloc(n * sizeof(int));
    if (v_corrige == NULL) {
        fprintf(stderr, "Erreur d'allocation de mémoire\n");
        exit(EXIT_FAILURE);
    }
    // Copier le vecteur v dans v_corrige
    for (unsigned int i = 0; i < n; i++) {
        v_corrige[i] = v[i];
    }
    // Si un indice est trouvé, inverser le bit à l'indice dans v_corrige
    if (indice != -1) {
        v_corrige[indice] = 1 - v_corrige[indice];
    }
    free(s);
    return v_corrige;
}

VECTEUR decode(VECTEUR v, unsigned int k, unsigned int n) {
    // Allouer de la mémoire pour le vecteur décodé
    VECTEUR v_decode = (VECTEUR)malloc(k * sizeof(int));
    if (v_decode == NULL) {
        fprintf(stderr, "Erreur d'allocation de mémoire\n");
        exit(EXIT_FAILURE);
    }
    // Copier les k premiers bits de v dans v_decodé
    for (unsigned int i = 0; i < k; i++) {
        v_decode[i] = v[i];
    }
    return v_decode;
}

int main() 
{
    int* G[] = {(int[]){1, 0, 0, 0, 1, 0, 1},
                (int[]){0, 1, 0, 0, 1, 1, 1},
                (int[]){0, 0, 1, 0, 1, 1, 0},
                (int[]){0, 0, 0, 1, 0, 1, 1}};
    unsigned int k = 4;
    unsigned int n = 7;

    // Générer tous les vecteurs possibles de taille k
    VECTEUR* vecteurs = mots(k);

    // Pour chaque vecteur, l'encoder avec G et le stocker dans le vecteur
    for (int i = 0; i < pow2(k); i++) {
        VECTEUR v = vecteurs[i];
        affiche_vecteur(v, k); // Afficher le vecteur original
        VECTEUR c = encode(G, v, k, n);
        affiche_vecteur(c, n); // Afficher le vecteur encodé
        free(vecteurs[i]); // Libérer l'ancien vecteur
        vecteurs[i] = c; // Stocker le nouveau vecteur encodé
    }

    VECTEUR* vecteurs2 = mots(4);
    printf("Encodage\n");
    for(int i =0; i < pow2(4); i++)
    {
        affiche_vecteur(vecteurs2[i], 4);
        affiche_vecteur(encode(G, vecteurs2[i], 4, 7), 7);
        printf("\n"); 
    }

    // Calculer et afficher la distance minimale
    unsigned int min_dist = dist_min(vecteurs, n, pow2(k));
    printf("La distance minimale est : %u\n", min_dist);

    // Calculer et afficher la capacité de décodage
    unsigned int e = (min_dist - 1) / 2;
    printf("La capacité de décodage est : %u\n", e);

    // Libérer la mémoire
    for (int i = 0; i < pow2(k); i++) {
        free(vecteurs[i]);
    }
    free(vecteurs);

    // Matrice de contrôle H
    int* H[] = {(int[]){1, 1, 1, 0, 1, 0, 0},
                (int[]){0, 1, 1, 1, 0, 1, 0},
                (int[]){1, 1, 0, 1, 0, 0, 1}};


    // Générer tous les vecteurs possibles de taille n
    VECTEUR* vecteurs_n = mots(n);

    // Pour chaque vecteur, calculer son syndrome avec H et l'afficher
    for (int i = 0; i < pow2(n); i++) {
        VECTEUR v = vecteurs_n[i];
        SYNDROME s = syndrome(H, v, k, n);
        printf("Vecteur : ");
        affiche_vecteur(v, n);
        printf("Syndrome : ");
        affiche_vecteur(s, n - k);
        free(vecteurs_n[i]); // Libérer l'ancien vecteur
        free(s); // Libérer le syndrome
    }

    
    //L'étude des syndromes peut nous aider à déterminer si un vecteur est un mot du code ou non.
    // Si le syndrome d'un vecteur est le vecteur nul, alors le vecteur est un mot du code. 
    // Sinon, le vecteur n'est pas un mot du code, et le syndrome donne une indication de l'erreur qui a été introduite dans le mot du code.
    

    // Libérer la mémoire 
    free(vecteurs_n);

    VECTEUR vecteurs_test[] = {(int[]){0, 0, 0, 0, 0, 0, 0},
                          (int[]){0, 1, 0, 0, 1, 1, 1},
                          (int[]){0, 0, 1, 0, 1, 1, 0},
                          (int[]){0, 1, 1, 0, 0, 0, 1},
                          (int[]){1, 1, 1, 0, 1, 0, 0},
                          (int[]){1, 0, 0, 1, 1, 1, 0},
                          (int[]){1, 0, 1, 1, 0, 0, 0}};
    unsigned int indices[] = {0, 1, 2, 3, 4, 5, 6};

    for (int i = 0; i < 7; i++) {
        VECTEUR v = vecteurs_test[i];
        unsigned int b = indices[i];

        // Calculer et afficher le syndrome original
        SYNDROME s = syndrome(G, v, k, n);
        printf("<");
        affiche_vecteur(v, n);
        printf("> - <");
        affiche_vecteur(s, n - k);
        printf("> -> ");

        // Bruiter le vecteur et calculer le nouveau syndrome
        VECTEUR v_bruite = bruite(v, n, b);
        SYNDROME s_bruite = syndrome(G, v_bruite, k, n);

        // Afficher le vecteur bruité et le nouveau syndrome
        printf("<");
        affiche_vecteur(v_bruite, n);
        printf("> - <");
        affiche_vecteur(s_bruite, n - k);
        printf(">\n");

        // Libérer la mémoire
        free(v_bruite);
        free(s_bruite);
        free(s);
    }

    return 0;
}