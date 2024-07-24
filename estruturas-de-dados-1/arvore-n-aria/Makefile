CC=g++

output: main.o Arvore.o NoArvore.o
	$(CC) main.o Arvore.o NoArvore.o -o output

main.o: main.cpp
	$(CC) -c main.cpp

Arvore.o: Arvore.cpp Arvore.hpp
	$(CC) -c Arvore.cpp

NoArvore.o: NoArvore.cpp NoArvore.hpp
	$(CC) -c NoArvore.cpp

clean:
	del *.o output.exe