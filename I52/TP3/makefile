main.exe: main.o
	g++ -Wall -g $^ -o main.exe
	valgrind ./main.exe

main.o: main.cpp
	g++ -c $^