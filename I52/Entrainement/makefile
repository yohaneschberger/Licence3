main.exe: main.o ct.o Element.o
	g++ -Wall -g $^ -o $@

main.o: main.cc ct.h
	g++ -c $^

ct.o: ct.cc ct.h
	g++ -c $^

Element.o: Element.cc Element.h ct.h
	g++ -c $^