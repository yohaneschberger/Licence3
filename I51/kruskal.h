#ifndef KRUSKAL_H
#define KRUSKAL_H
#include "graphe.h"

typedef struct point{
  float x;
  float y;
}point;

typedef struct nuage{
  point* pts;
  int nbs;
}nuage;

typedef struct arete{
  int i;
  int j;
  float w;
}arete;

float dist(point p1,point p2);
nuage creerNuage(int n);
graphe kruskal(nuage N);
void Parcours(graphe *g);
void PPR(int s, graphe *g, int *ptr,int *v);


#endif
