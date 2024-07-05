#ifndef STRUCT_H
#define STRUCT_H

typedef struct ed{
  struct ed* route;
  int s;
  int rang;
}enrdisjoint, *disjoint;

disjoint singleton(int s);
disjoint representant(disjoint s);
void reunion(disjoint u, disjoint v);

#endif
