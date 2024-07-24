#include "NoArvoreBinaria.hpp"
#include <string>
using namespace std;


class ArvoreBinaria
{
private:
    NoArvoreBinaria* raiz;

    bool pertence(NoArvoreBinaria* no, int info);
    int pares(NoArvoreBinaria* no);
    int folhas(NoArvoreBinaria* no);
    string preOrdem(NoArvoreBinaria* no);
    string emOrdem(NoArvoreBinaria* no);
    string posOrdem(NoArvoreBinaria* no);
    int numNos(NoArvoreBinaria* no);
    int altura(NoArvoreBinaria* no);
    bool igual(NoArvoreBinaria* no1, NoArvoreBinaria* no2);

public:
    ArvoreBinaria();

    NoArvoreBinaria* getRaiz();

    NoArvoreBinaria* insere(int v, NoArvoreBinaria* esq, NoArvoreBinaria* dir);
    bool vazia();
    bool pertence(int info);
    int pares();
    int folhas();
    string preOrdem();
    string emOrdem();
    string posOrdem();
    int numNos();
    int altura();
    bool igual(ArvoreBinaria* a);
};