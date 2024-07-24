CC=g++

output: main.o ArvoreBinaria.o NoArvoreBinaria.o
	$(CC) main.o ArvoreBinaria.o NoArvoreBinaria.o -o output

main.o: main.cpp
	$(CC) -c main.cpp

ArvoreBinaria.o: ArvoreBinaria.cpp ArvoreBinaria.hpp
	$(CC) -c ArvoreBinaria.cpp

NoArvoreBinaria.o: NoArvoreBinaria.cpp NoArvoreBinaria.hpp
	$(CC) -c NoArvoreBinaria.cpp

clean:
	del *.o output.exe