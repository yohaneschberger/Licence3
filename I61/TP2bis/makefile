CC = gcc
src = $(wildcard *.c)

main.o : $(src)
	$(CC) -g -Wall $^ -o tp2
	valgrind --leak-check=full ./tp2