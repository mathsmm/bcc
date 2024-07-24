#include "ArvoreBinaria.hpp"
#include <iostream>
using namespace std;


int main()
{
    /* Árvore construída:
     *        9
     *      /   \
     *     /     \
     *    5       8
     *          /   \
     *         /     \
     *        6       7
     *       / \     / \
     *      1   2   3   4
     */

    NoArvoreBinaria* f1 = new NoArvoreBinaria(1);
    NoArvoreBinaria* f2 = new NoArvoreBinaria(2);
    NoArvoreBinaria* f3 = new NoArvoreBinaria(3);
    NoArvoreBinaria* f4 = new NoArvoreBinaria(4);
    NoArvoreBinaria* f5 = new NoArvoreBinaria(5);
    NoArvoreBinaria* n1 = new NoArvoreBinaria(6, f1, f2);
    NoArvoreBinaria* n2 = new NoArvoreBinaria(7, f3, f4);
    NoArvoreBinaria* n3 = new NoArvoreBinaria(8, n1, n2);
    ArvoreBinaria* arvore = new ArvoreBinaria();
    arvore->insere(9, f5, n3);

    cout << "Pre-ordem: " << arvore->preOrdem() << endl;
    cout << "Em-ordem:  " << arvore->emOrdem()  << endl;
    cout << "Pos-ordem: " << arvore->posOrdem() << endl;
    cout << "\n";

    cout << "Numero 9 pertence a arvore? "  << arvore->pertence(9)  << endl;
    cout << "Numero 2 pertence a arvore? "  << arvore->pertence(2)  << endl;
    cout << "Numero 11 pertence a arvore? " << arvore->pertence(11) << endl;
    cout << "\n";

    cout << "Quantidade de pares: " << arvore->pares() << endl;
    cout << "Numero de folhas: " << arvore->folhas() << endl;
    cout << "Numero de nos (sem contar as folhas): " << arvore->numNos() << endl;
    cout << "Altura da arvore: " << arvore->altura() << endl;
    cout << "\n";

    NoArvoreBinaria* f10 = new NoArvoreBinaria(1);
    NoArvoreBinaria* f20 = new NoArvoreBinaria(2);
    NoArvoreBinaria* f30 = new NoArvoreBinaria(3);
    NoArvoreBinaria* f40 = new NoArvoreBinaria(4);
    NoArvoreBinaria* f50 = new NoArvoreBinaria(5);
    NoArvoreBinaria* n10 = new NoArvoreBinaria(6, f10, f20);
    NoArvoreBinaria* n20 = new NoArvoreBinaria(7, f30, f40);
    NoArvoreBinaria* n30 = new NoArvoreBinaria(8, n10, n20);
    ArvoreBinaria* arvore2 = new ArvoreBinaria();
    arvore2->insere(9, f50, n30);
    
    cout << "Arvore 1: " << arvore->preOrdem()  << endl;
    cout << "Arvore 2: " << arvore2->preOrdem() << endl;
    cout << "Arvore 1 eh igual a arvore 2? " << arvore->igual(arvore2) << endl;
    cout << "\n";

    arvore2->insere(10, arvore2->getRaiz(), nullptr);

    cout << "Arvore 1: " << arvore->preOrdem()  << endl;
    cout << "Arvore 2: " << arvore2->preOrdem() << endl;
    cout << "Depois de alterar a arvore 2, continuam iguais? " << arvore->igual(arvore2) << endl;

    return 0;
}