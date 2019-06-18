CC=g++

wadsworth: butler.o main.o
	$(CC) -Wall butler.o main.o -o wadsworth
butler.o: butler.cc butler.h
	$(CC) -c butler.cc
main.o:	main.cc butler.h
	$(CC) -c main.cc
clean:
	rm -r *.o wadsworth
