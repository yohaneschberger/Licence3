#include <stdio.h>
#include <stdlib.h>

#include "graphe.h"
#include "kruskal.h"


void DessinerNuage(point *pts, int n){
	FILE *dst;
	char name[128] = "nuage.dot";
	char cmd[1028];
	dst = fopen("nuage.dot", "w");
	if (dst == NULL ) {
		perror("erreur fonction DessinerGraphe");
		exit(1);

	}
	fprintf(dst, "graph nuage {\n" );
	fprintf(dst, "node [shape=circle]\n");
	for (int i = 0; i < n; ++i) {
    fprintf(dst,"%d [pos = \"%f,%f!\" ];\n",i,pts[i].x,pts[i].y);
	}
	fputc('}',dst);
	fclose(dst);
	sprintf(cmd, "dot -Kfdp -n -Tpng %s -o nuage.png", name);

	system(cmd);
}

void DessinerArbre(point *pts, graphe g){
	FILE *dst;
	char name[128] = "arbre.dot";
	char cmd[1028];
	dst = fopen("arbre.dot", "w");
	if (dst == NULL ) {
		perror("erreur fonction DessinerGraphe");
		exit(1);

	}
	fprintf(dst, "graph arbre {\n" );
	fprintf(dst, "node [shape=circle]\n");
	for (int i = 0; i < g.nbs; ++i) {
    fprintf(dst,"%d [pos = \"%f,%f!\" ];\n",i,pts[i].x,pts[i].y);
	}
	for(int i = 0; i < g.nbs;i++)
	{
		for(int j = i+1; j<g.nbs;j++)
		{
			if(g.mat[i][j]==1)
				fprintf(dst, "%d--%d\n",i,j );
		}
	}
	fputc('}',dst);
	fclose(dst);
	sprintf(cmd, "dot -Kfdp -n -Tpng %s -o arbre.png", name);

	system(cmd);
}


void DessinerParcours(point *pts, graphe g){
	FILE *dst;
	char name[128] = "parcours.dot";
	char cmd[1028];
	dst = fopen("parcours.dot", "w");
	if (dst == NULL ) {
		perror("erreur fonction DessinerGraphe");
		exit(1);

	}
	fprintf(dst, "graph parcours {\n" );
	fprintf(dst, "node [shape=circle color=red]\n");
	fprintf(dst, "edge [color=red]\n");
	for (int i = 0; i < g.nbs; ++i) {
    fprintf(dst,"%d [pos = \"%f,%f!\" ];\n",i,pts[i].x,pts[i].y);
	}
	for(int i = 0; i < g.nbs;i++)
	{
		for(int j = i+1; j<g.nbs;j++)
		{
			if(g.mat[i][j]==1)
				fprintf(dst, "%d--%d\n",i,j );
		}
	}
	for(int i = 1;i<g.nbs;i++)
	{
		fprintf(dst,"%d--%d[color=black label=\"%d\"]\n",g.tab[i-1],g.tab[i],i-1);
	}
	fprintf(dst,"%d--%d[color=black label=\"%d\"]\n",g.tab[0],g.tab[g.nbs-1],g.nbs-1);
	fputc('}',dst);
	fclose(dst);
	sprintf(cmd, "dot -Kfdp -n -Tpng %s -o parcours.png", name);

	system(cmd);
}



int main(int argc, char const *argv[]) {
    int n = atoi(argv[1]);
    nuage N = creerNuage(n);
    DessinerNuage(N.pts,n);
    graphe g = kruskal(N);
	DessinerArbre(N.pts,g);
	Parcours(&g);
	DessinerParcours(N.pts,g);
    return 0;
}
