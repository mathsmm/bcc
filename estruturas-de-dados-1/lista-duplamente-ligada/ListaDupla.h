#pragma once
#include "NoListaDupla.h"

class ListaDupla {
    public:
        NoListaDupla *prim;
        
        ListaDupla();
        void insere(int v);
        void imprime();
        bool vazia();
        NoListaDupla *busca(int v);
        int comprimento();
        NoListaDupla *ultimo();
        void retira(int v);
        void libera();
        void insereFim(int v);
        bool igual(ListaDupla l);
        void merge(ListaDupla l);
}; 