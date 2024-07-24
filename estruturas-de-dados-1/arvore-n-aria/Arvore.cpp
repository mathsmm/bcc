#include "Arvore.hpp"
#include <iostream>

Arvore::Arvore():
    raiz{nullptr}
{}

NoArvore* Arvore::criaNo(int info)
{
    NoArvore* novo_no = new NoArvore(info);
    raiz = novo_no;
    return novo_no;
}

void Arvore::insereFilho(NoArvore* no, NoArvore* sa)
{
    sa->setProx(no->getPrim());
    no->setPrim(sa);
    raiz = no;
}

std::string Arvore::toString()
{
    return imprime(raiz);
}

std::string Arvore::imprime(NoArvore* no)
{
    std::string s = "";
    s += "<" + std::to_string(no->getInfo());

    NoArvore* p = no->getPrim();
    while (p != nullptr)
    {
        s += imprime(p);
        p = p->getProx();
    }
    s += ">";
    return s;
}

bool Arvore::pertence(int info)
{
    return pertence(raiz, info);
}

bool Arvore::pertence(NoArvore* no, int info)
{
    if (no->getInfo() == info)
    {
        return true;
    }

    NoArvore* p = no->getPrim();
    
    while (p != nullptr)
    {
        if (pertence(p, info))
        {
            return true;
        }

        p = p->getProx();
    }

    return false;
}

int Arvore::altura()
{
    return altura(raiz);
}

int Arvore::altura(NoArvore* no)
{
    int hmax = -1;
    NoArvore* p = no->getPrim();

    while (p != nullptr)
    {
        int h = altura(p);

        if (h > hmax)
        {
            hmax = h;
        }

        p = p->getProx();
    }

    return hmax + 1;
}

int Arvore::pares()
{
    return pares(raiz);
}

int Arvore::pares(NoArvore* no)
{
    int qtdPares = 0;
    NoArvore* p = no->getPrim();

    while (p != nullptr)
    {
        qtdPares += 
            (p->getInfo() % 2 == 0)
            ? 1
            : 0;

        qtdPares += pares(p);

        p = p->getProx();
    }

    return qtdPares;
}

int Arvore::folhas()
{
    return folhas(raiz);
}

int Arvore::folhas(NoArvore* no)
{
    int qtdFolhas = 0;
    NoArvore* p = no->getPrim();

    if (p == nullptr)
    {
        return 0;
    }

    while (p != nullptr)
    {
        qtdFolhas += folhas(p);

        p = p->getProx();
    }

    return 1 + qtdFolhas;
}

bool Arvore::igual(Arvore* a)
{
    return (toString() == a->toString());
}