main.exe: main.o serie.o episode.o saison.o
	g++ -Wall main.o serie.o episode.o saison.o -o main.exe

main.o: main.cc serie.h episode.h saison.h
	g++ -c main.cc

serie.o: serie.cc serie.h
	g++ -c serie.cc

episode.o: episode.cc episode.h serie.h
	g++ -c episode.cc

saison.o: saison.cc episode.h
	g++ -c saison.cc