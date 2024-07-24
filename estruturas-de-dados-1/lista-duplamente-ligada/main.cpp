#include "ListaDupla.h"
#include <iostream>
using namespace std;

int main()
{
    ListaDupla lista1;
    ListaDupla lista2;
    
    lista1.insere(3);
    lista1.insere(2);
    lista1.insere(1);
    
    lista2.insere(6);
    lista2.insere(5);
    lista2.insere(4);
    
    cout << "Lista 1:" << endl;
    lista1.imprime();
    
    cout << endl << "Lista 2:" << endl;
    lista2.imprime();
    
    cout << endl << "Comprimento da lista 1: " << lista1.comprimento() << endl;
    cout <<         "Comprimento da lista 2: " << lista2.comprimento() << endl;
    
    lista1.insereFim(4);
    lista2.insereFim(7);
    
    cout << endl << "Lista 1 após inseção no fim:" << endl;
    lista1.imprime();
    
    cout << endl << "Lista 2 após inserção no fim:" << endl;
    lista2.imprime();
    
    lista1.retira(2);
    lista2.retira(5);
    
    cout << endl << "Lista 1 após remoção:" << endl;
    lista1.imprime();
    
    cout << endl << "Lista 2 após remoção:" << endl;
    lista2.imprime();
    
    cout << endl << "Lista 1 é igual à lista 2? " << lista1.igual(lista2) << endl;
    
    lista1.merge(lista2);
    
    cout << endl << "Lista 1 após execução do merge com a lista 2:" << endl;
    lista1.imprime();
    
    lista1.libera();
    lista2.libera();
    
    return 0;
}