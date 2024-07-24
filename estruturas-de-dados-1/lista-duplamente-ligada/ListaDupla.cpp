#include "ListaDupla.h"
#include <iostream>

ListaDupla::ListaDupla():
    prim{ NULL }
{}

void ListaDupla::insere(int v) {
    NoListaDupla *novo_no = new NoListaDupla(v);
    
    if (this->prim != NULL) {
        prim->ant = novo_no;
        novo_no->prox = prim;
    } else {
        novo_no->prox = NULL;
    }
    
    prim = novo_no;
}

void ListaDupla::imprime() {
    NoListaDupla *no_atual = prim;
    
    while (no_atual != NULL) {
        std::cout << no_atual->info << std::endl;
        no_atual = no_atual->prox;
    }
}


bool ListaDupla::vazia() {
    return (prim == NULL);
}


NoListaDupla* ListaDupla::busca(int v) {
    NoListaDupla *no_atual = prim;
    
    while (no_atual->info != v) {
        no_atual = no_atual->prox;
        
        if (no_atual == NULL) {
            return NULL;
        }
    }
    
    return no_atual;
}


int ListaDupla::comprimento() {
    NoListaDupla *no_atual = prim;
    int i = 0;
    
    while (no_atual != NULL) {
        no_atual = no_atual->prox;
        i++;
    }
    
    return i;
}


NoListaDupla* ListaDupla::ultimo() {
    NoListaDupla *no_atual = prim;
    
    while (no_atual->prox != NULL) {
        no_atual = no_atual->prox;
    }
    
    return no_atual;
}


void ListaDupla::retira(int v) {
    NoListaDupla *no_ant   = NULL;
    NoListaDupla *no_atual = prim;

    while (no_atual != NULL && no_atual->info != v) {
        no_ant   = no_atual;
        no_atual = no_atual->prox;
        
        if (no_atual == NULL) {
            return;
        }
    }
    
    if (no_ant == NULL) {
        prim = no_atual->prox;
    } else {
        no_ant->prox = no_atual->prox;
    }
    
    if (no_atual->prox != NULL) {
        no_atual->prox->ant = no_ant;
    }
    
    delete no_atual;
}


void ListaDupla::libera() {
    NoListaDupla* no_atual = prim;

    while (no_atual != NULL) {
        NoListaDupla* prox_no = no_atual->prox;
        delete no_atual;
        no_atual = prox_no;
    }

    prim = NULL;
}


void ListaDupla::insereFim(int v) {
    NoListaDupla* novo_no = new NoListaDupla(v);

    if (prim == NULL) {
        prim = novo_no;
        return;
    }

    NoListaDupla* no_atual = prim;

    while (no_atual->prox != NULL) {
        no_atual = no_atual->prox;
    }

    no_atual->prox = novo_no;
    novo_no->ant = no_atual;
}


bool ListaDupla::igual(ListaDupla l) {
    NoListaDupla* no_atual_1 = prim;
    NoListaDupla* no_atual_2 = l.prim;
    
    while (no_atual_1 != NULL && no_atual_2 != NULL) {

        if (no_atual_1->info != no_atual_2->info) {
            return false;
        }

        no_atual_1 = no_atual_1->prox;
        no_atual_1 = no_atual_2->prox;
    }
    
    return (no_atual_1 == NULL && no_atual_2 == NULL);
}


void ListaDupla::merge(ListaDupla l) {
    NoListaDupla* no_atual_1 = prim;
    NoListaDupla* no_atual_2 = l.prim;
    NoListaDupla* no_ant     = NULL;
    
    while (no_atual_1 != NULL && no_atual_2 != NULL) {
        NoListaDupla* no_prox_1 = no_atual_1->prox;
        NoListaDupla* no_prox_2 = no_atual_2->prox;
        
        no_atual_1->ant  = no_ant;
        no_atual_2->ant  = no_atual_1;
        no_atual_1->prox = no_atual_2;
        no_atual_2->prox = no_prox_1;
        
        no_ant     = no_atual_2;
        no_atual_1 = no_prox_1;
        no_atual_2 = no_prox_2;
    }
    
    if (no_atual_2 != NULL) {
        if (no_ant != NULL) {
            no_ant->prox    = no_atual_2;
            no_atual_2->ant = no_ant;
        } else {
            prim = no_atual_2;
            no_atual_2->ant = NULL;
        }
    }
}