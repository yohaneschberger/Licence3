OPTIONS = -Wall -g
OBJETS = disjoint.o graphe.o kruskal.o

main.exe: main.o $(OBJETS)
	gcc $(OPTIONS) main.o $(OBJETS) -o $@ -lm

main.o: main.c kruskal.h disjoint.h graphe.h
	gcc $(OPTIONS) -c $^

kruskal.o: kruskal.c kruskal.h disjoint.h graphe.h
	gcc $(OPTIONS) -c $^

disjoint.o: disjoint.c disjoint.h
	gcc $(OPTIONS) -c $^

graphe.o: graphe.c graphe.h
	gcc $(OPTIONS) -c $^

clean:
	rm *.o *.dat
