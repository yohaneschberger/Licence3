#ifndef LISTE_H
#define LISTE_H

#include <stdio.h>

typedef struct liste
{
  int num;
  struct liste *svt;
} enr, *liste;

typedef struct
{
  int nbs;
  int **mat;
  char* idt;
  liste *adj;
  int *tab;
} graphe;

graphe InitGraphe(int n);
graphe aleatoire(float p, int n);
void liberer(graphe G);


#endif
