#include <iostream>
#include "Arvore.hpp"
using namespace std;

int main()
{
    Arvore a1;

    NoArvore* n1  = a1.criaNo(1);
    NoArvore* n2  = a1.criaNo(2);
    NoArvore* n3  = a1.criaNo(3);
    NoArvore* n4  = a1.criaNo(4);
    NoArvore* n5  = a1.criaNo(5);
    NoArvore* n6  = a1.criaNo(6);
    NoArvore* n7  = a1.criaNo(7);
    NoArvore* n8  = a1.criaNo(8);
    NoArvore* n9  = a1.criaNo(9);
    NoArvore* n10 = a1.criaNo(10);

    a1.insereFilho(n3, n4);
    a1.insereFilho(n2, n5);
    a1.insereFilho(n2, n3);
    a1.insereFilho(n9, n10);
    a1.insereFilho(n7, n9);
    a1.insereFilho(n7, n8);
    a1.insereFilho(n1, n7);
    a1.insereFilho(n1, n6);
    a1.insereFilho(n1, n2);

    cout << "Arvore 1: " << a1.toString() << endl;
    cout << "Numero 9 pertence a arvore 1? "  << a1.pertence(9)  << endl;
    cout << "Numero 11 pertence a arvore 1? " << a1.pertence(11) << endl;
    cout << "Altura da arvore 1: " << a1.altura() << endl;
    cout << "Qtd de pares da arvore 1: " << a1.pares() << endl;
    cout << "Qtd de folhas da arvore 1: " << a1.folhas() << endl;

    Arvore a2;

    NoArvore* n11  = a2.criaNo(1);
    NoArvore* n20  = a2.criaNo(2);
    NoArvore* n30  = a2.criaNo(3);
    NoArvore* n40  = a2.criaNo(4);
    NoArvore* n50  = a2.criaNo(5);
    NoArvore* n60  = a2.criaNo(6);
    NoArvore* n70  = a2.criaNo(7);
    NoArvore* n80  = a2.criaNo(8);
    NoArvore* n90  = a2.criaNo(9);
    NoArvore* n100 = a2.criaNo(10);

    a2.insereFilho(n30, n40);
    a2.insereFilho(n20, n50);
    a2.insereFilho(n20, n30);
    a2.insereFilho(n90, n100);
    a2.insereFilho(n70, n90);
    a2.insereFilho(n70, n80);
    a2.insereFilho(n11, n70);
    a2.insereFilho(n11, n60);
    a2.insereFilho(n11, n20);

    cout << "\n";

    cout << "Arvore 2: " << a2.toString() << endl;
    cout << "Arvore 1 eh igual a arvore 2? " << a1.igual(&a2) << endl;

    NoArvore* n110 = a2.criaNo(11);
    a2.insereFilho(n11, n110);

    cout << "Arvore 2 depois de ser alterada: " << a2.toString() << endl;
    cout << "Arvore 1 continua igual a arvore 2? " << a1.igual(&a2) << endl;


    return 0;
}