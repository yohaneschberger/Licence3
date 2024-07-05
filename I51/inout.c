#include <stdio.h>
#include <stdlib.h>

#include "inout.h"

graphe lireGraphe(char* nom)
{
  FILE *src;
  src = fopen(nom, "r");
  if(src==NULL)
  {
    perror(nom);
    exit(1);
  }
  graphe res;
  char buffer[1024];
  while(fgets(buffer,1024,src))
  {
    int n;
    switch (buffer[0]) {
      case 'n': if(sscanf(buffer,"nbs=%d",&n))
                  {
                    res = InitGraphe(n);
                  break;}

      case '#': break;
    }
    int i, j;
     if(sscanf(buffer,"%d %d", &i, &j) == 2)
    {
      res.mat[i][j] = res.mat[j][i] = 1;
    }
  }
  return res;
}

void dessiner(char* nom, graphe g)
{
  FILE* dst;
  char fn[64];
  sprintf(fn,"%s.dot",nom);
  dst = fopen(fn, "w");
  if(!dst)
  {
    perror(nom);
    exit(1);
  }
  fputs("graph{", dst);
  fputc('\n', dst);
  int i, j;
  for(i = 0; i < g.nbs; i++)
    for(j = i+1; j < g.nbs; j++)
      if(g.mat[i][j])
        fprintf(dst, "%d--%d\n",i,j);
  fputc('\n', dst);
  fputs("}", dst);
  fclose(dst);
  char cmd[128];
  sprintf(cmd, "dot -Tpng %s -o %s.png; eog %s.png", fn, nom, nom);
  system(cmd);
}
