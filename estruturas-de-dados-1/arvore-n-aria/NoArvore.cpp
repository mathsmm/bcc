#include "NoArvore.hpp"


NoArvore::NoArvore(int info):
    info{info},
    prim{nullptr},
    prox{nullptr}
{}

void NoArvore::setInfo(int info)
{
    this->info = info;
}

int NoArvore::getInfo()
{
    return info;
}

void NoArvore::setPrim(NoArvore* prim)
{
    this->prim = prim;
}

NoArvore* NoArvore::getPrim()
{
    return prim;
}

void NoArvore::setProx(NoArvore* prox)
{
    this->prox = prox;
}

NoArvore* NoArvore::getProx()
{
    return prox;
}

std::string NoArvore::toString()
{
    return std::to_string(info);
}
