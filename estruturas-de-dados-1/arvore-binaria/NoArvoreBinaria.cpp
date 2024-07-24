#include "NoArvoreBinaria.hpp"


NoArvoreBinaria::NoArvoreBinaria(int info):
    info{info},
    sae{nullptr},
    sad{nullptr}
{}

NoArvoreBinaria::NoArvoreBinaria(int info, NoArvoreBinaria* esq, NoArvoreBinaria* dir):
    info{info},
    sae{esq},
    sad{dir}
{}

int NoArvoreBinaria::getInfo()
{
    return info;
}

void NoArvoreBinaria::setInfo(int info)
{
    this->info = info;
}

NoArvoreBinaria* NoArvoreBinaria::getSae()
{
    return sae;
}

void NoArvoreBinaria::setSae(NoArvoreBinaria* esq)
{
    sae = esq;
}

NoArvoreBinaria* NoArvoreBinaria::getSad()
{
    return sad;
}

void NoArvoreBinaria::setSad(NoArvoreBinaria* dir)
{
    sad = dir;
}