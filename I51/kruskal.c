#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <assert.h>

#include "kruskal.h"
#include "disjoint.h"

static int compare(const void * ptr1, const void * ptr2)
{
  float x, y;
  x = ((arete*)ptr1)->w;
  y = ((arete*)ptr2)->w;
  if(x < y) return -1;
  if(x > y) return 1;
  return 0;
}

float dist(point p1,point p2)
{
  float dx, dy, dres;
  dx = p2.x - p1.x;
  dy = p2.y - p1.y;
  dres = dx*dx + dy*dy;
  return sqrt(dres);
}

nuage creerNuage(int n)
{
  nuage res;
  srand(time(NULL));
  res.nbs = n;
  res.pts = calloc(n, sizeof(point));
  for(int i = 0; i<n; i++)
  {
    float r = rand();
    r = (r-RAND_MAX/2) / RAND_MAX*2;
    res.pts[i].x = r;
    r = rand();
    r = (r-RAND_MAX/2) / RAND_MAX*2;
    res.pts[i].y = r;
  }
  return res;
}

graphe kruskal(nuage N)
{
  graphe res = InitGraphe(N.nbs);
  int m = N.nbs*(N.nbs-1)/2;
  arete *a = calloc(m, sizeof(arete));
  int i, j, k = 0;
  for(i = 0; i < N.nbs; i++)
  {
    for(j = i+1; j < N.nbs; j++)
    {
      a[k].i = i;
      a[k].j = j;
      a[k].w = dist(N.pts[i], N.pts[j]);
      k++;
    }
  }
  assert(k==m);
  qsort(a, m, sizeof(arete), compare);
  disjoint *tab = calloc(N.nbs, sizeof(disjoint));
  for(i = 0; i < N.nbs; i++)
    tab[i] = singleton(i);
  k = 0;
  int p = N.nbs;
  while(p > 1)
  {
    i = a[k].i;
    j = a[k].j;
    disjoint ri = representant(tab[i]);
    disjoint rj = representant(tab[j]);
    if(ri != rj){
      reunion(ri, rj);
      p--;
      res.mat[i][j] = 1;
      res.mat[j][i] = 1;
    }
    k++;
  }
  free(a);
  free(tab);
  return res;
}

void Parcours(graphe *g)
{
  int *v = calloc(g->nbs, sizeof(int));
  g->tab = calloc(g->nbs, sizeof(int));
  int ptr = 0;
  PPR(0, g, &ptr ,v);
 free(v);
}

void PPR(int s, graphe *g, int *ptr, int *v)
{
 g->tab[*ptr] = s;
 *ptr = *ptr + 1;
 v[s] = 1;
 int i;
 for(i = 0; i < g->nbs; i++)
 {
   if(v[i] == 0 && g->mat[i][s] == 1)
     PPR(i, g, ptr, v);
 }
}
