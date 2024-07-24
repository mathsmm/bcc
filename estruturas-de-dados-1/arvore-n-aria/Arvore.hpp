#include "NoArvore.hpp"
#include <string>

class Arvore
{
private:
    NoArvore* raiz;

    std::string imprime(NoArvore* no);
    bool pertence(NoArvore* no, int info);
    int altura(NoArvore* no);
    int pares(NoArvore* no);
    int folhas(NoArvore* no);

public:
    Arvore();
    NoArvore* criaNo(int info);
    std::string toString();
    void insereFilho(NoArvore* no, NoArvore* sa);
    bool pertence(int info);
    int  altura();
    int  pares();
    int  folhas();
    bool igual(Arvore* a);
    // Arvore* copia();
};