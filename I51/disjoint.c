#include <stdio.h>
#include <stdlib.h>

#include "disjoint.h"

disjoint singleton(int n)
{
  disjoint r = malloc(sizeof(enrdisjoint));
  r->s = n;
  r->route = r;
  r->rang = 0;

  return r;
}

disjoint representant(disjoint s)
{
  if(s->route == s) return s;
  return s->route = representant(s->route);
}

void reunion(disjoint u, disjoint v)
{
  if(u -> rang == v -> rang)
    u -> rang++;

  if(u -> rang < v -> rang)
  {
    u -> route = v;
  }
  else v -> route = u;
}
