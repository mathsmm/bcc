#pragma once

class NoListaDupla {
    public:
        int info;
        NoListaDupla *ant;
        NoListaDupla *prox;
        
        NoListaDupla(int v);
};