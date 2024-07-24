#include "ArvoreBinaria.hpp"
#include <string>
#include<algorithm>


ArvoreBinaria::ArvoreBinaria():
    raiz{nullptr}
{}

NoArvoreBinaria* ArvoreBinaria::getRaiz()
{
    return raiz;
}

NoArvoreBinaria* ArvoreBinaria::insere(int v, NoArvoreBinaria* esq, NoArvoreBinaria* dir)
{
    NoArvoreBinaria* novoNo = new NoArvoreBinaria(v, esq, dir);
    raiz = novoNo;
    return novoNo;
}

bool ArvoreBinaria::vazia()
{
    return raiz == nullptr;
}

bool ArvoreBinaria::pertence(int info)
{
    return pertence(raiz, info);
}

bool ArvoreBinaria::pertence(NoArvoreBinaria* no, int info)
{
    if (no == nullptr)
    {
        return false;
    }

    return (
        (no->getInfo()      == info) || 
        pertence(no->getSae(), info) || 
        pertence(no->getSad(), info)
    );
}

int ArvoreBinaria::pares()
{
    return pares(raiz);
}

int ArvoreBinaria::pares(NoArvoreBinaria* no)
{
    if (no == nullptr)
    {
        return 0;
    }

    return 
        ((no->getInfo() % 2) == 0)
        ? 1 + pares(no->getSae()) + pares(no->getSad())
        : 0 + pares(no->getSae()) + pares(no->getSad());
}

int ArvoreBinaria::folhas()
{
    return folhas(raiz);
}

int ArvoreBinaria::folhas(NoArvoreBinaria* no)
{
    if (no == nullptr)
    {
        return 0;
    }

    return 
        ((no->getSae() == nullptr) && (no->getSad() == nullptr))
        ? 1
        : folhas(no->getSae()) + folhas(no->getSad());
}

string ArvoreBinaria::preOrdem()
{
    return preOrdem(raiz);
}

string ArvoreBinaria::preOrdem(NoArvoreBinaria* no)
{
    string s = "<";
    if (no != nullptr)
    {
        s += 
            std::to_string(no->getInfo()) + 
            preOrdem(no->getSae()) + 
            preOrdem(no->getSad());
    }
    s += ">";
    return s;
}

string ArvoreBinaria::emOrdem()
{
    return emOrdem(raiz);
}

string ArvoreBinaria::emOrdem(NoArvoreBinaria* no)
{
    string s = "<";
    if (no != nullptr)
    {
        s += 
            emOrdem(no->getSae()) + 
            std::to_string(no->getInfo()) + 
            emOrdem(no->getSad());
    }
    s += ">";
    return s;
}

string ArvoreBinaria::posOrdem()
{
    return posOrdem(raiz);
}

string ArvoreBinaria::posOrdem(NoArvoreBinaria* no)
{
    string s = "<";
    if (no != nullptr)
    {
        s += 
            posOrdem(no->getSae()) + 
            posOrdem(no->getSad()) + 
            std::to_string(no->getInfo());
    }
    s += ">";
    return s;
}

int ArvoreBinaria::numNos()
{
    return numNos(raiz);
}

int ArvoreBinaria::numNos(NoArvoreBinaria* no)
{
    if (no == nullptr) 
    {
        return 0;
    }

    return
        ((no->getSae() != nullptr) || (no->getSad() != nullptr))
        ? 1 + numNos(no->getSae()) + numNos(no->getSad())
        : 0; //folha
}

int ArvoreBinaria::altura()
{
    return altura(raiz);
}

int ArvoreBinaria::altura(NoArvoreBinaria* no)
{
    if (no == nullptr)
    {
        return 0;
    }

    return 1 + std::max(altura(no->getSae()), altura(no->getSad()));
}

bool ArvoreBinaria::igual(ArvoreBinaria* a) {
    return igual(raiz, a->raiz);
}

bool ArvoreBinaria::igual(NoArvoreBinaria* no1, NoArvoreBinaria* no2) {
    if (no1 == nullptr && no2 == nullptr) {
        return true;
    }

    if (no1->getInfo() != no2->getInfo()) {
        return false;
    }

    if (no1 == nullptr || no2 == nullptr) {
        return false;
    }

    return igual(no1->getSae(), no2->getSae()) && igual(no1->getSad(), no2->getSad());
}