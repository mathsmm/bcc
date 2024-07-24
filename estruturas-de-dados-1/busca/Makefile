CC=g++

output: main.o Vetor.o Busca.o
	$(CC) main.o Vetor.o Busca.o -o output

main.o: main.cpp
	$(CC) -c main.cpp

Vetor.o: Vetor.cpp
	$(CC) -c Vetor.cpp

Busca.o: Busca.cpp
	$(CC) -c Busca.cpp

clean:
	del *.o output.exe