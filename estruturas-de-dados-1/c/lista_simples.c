#include <stdio.h>
#include <stdlib.h>
#include "lista_simples.h"

NoLista *sllCria(void) 
{
    // Uma lista vazia é simplesmente um objeto nulo
    return NULL;
}

NoLista *sllInsere(NoLista *head, int v) 
{
    NoLista *novo = malloc(sizeof(NoLista));
    novo->prox = head;
    novo->info = v;

    return novo;
}

void sllImprime(NoLista *head) 
{
    NoLista *aux = head;

    while (aux != NULL) {
        printf("%d\n", aux->info);
        aux = aux->prox;
    }
}

int sllVazia(NoLista *head) {
    return head == NULL;
}

NoLista *sllBusca(NoLista *head, int v) 
{
    NoLista *aux = head;

    while (aux != NULL) {
        if (aux->info == v)
            return aux;

        aux = aux->prox;
    }

    return NULL;
}

int sllComprimento(NoLista *head) 
{
    NoLista *aux = head;
    int i = 0;

    while (aux != NULL) {
        aux = aux->prox;
        i++;
    }

    return i;
}

NoLista *sllUltimo(NoLista *head) 
{
    if (head == NULL)
        return NULL;

    NoLista *aux = head;

    while (aux->prox != NULL) {
        aux = aux->prox;
    }

    return aux;
}