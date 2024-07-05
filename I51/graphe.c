#include <stdio.h>
#include <stdlib.h>
#include <time.h>

typedef unsigned char uchar;

#include "graphe.h"

graphe InitGraphe(int n)
{
  graphe res;
  res.nbs = n;
  res.mat = calloc(n, sizeof(uchar*));
  int i;
  for(i=0; i<n; i++)
    res.mat[i] = calloc(n, sizeof(uchar));
  res.adj = calloc(n, sizeof(liste));
  return res;
}

graphe aleatoire(float p, int n)
{
  srand(time(NULL));
  int s = p * RAND_MAX;
  graphe res = InitGraphe(n);

  for(int i=0; i<n; i++)
    for(int j=i+1; j<n; j++)
      if(random() <= s)
        res.mat[i][j] = res.mat[j][i] = 1;

  return res;
}

void liberer(graphe G)
{
  int i;
  liste aux;
  for(i=0; i<G.nbs; i++)
    free(G.mat[i]);
  free(G.mat);
  for(i=0; i<G.nbs; i++)
    while (G.adj[i]) {
      aux = G.adj[i];
      G.adj[i] = aux->svt;
      free(aux);
    }
  free(G.adj);
}
