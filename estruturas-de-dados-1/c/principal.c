#include <stdio.h>
#include "lista_simples.h"

int main() 
{
    NoLista *lista = sllCria();

    lista = sllInsere(lista,  10);
    lista = sllInsere(lista, -15);
    lista = sllInsere(lista,  8);
    lista = sllInsere(lista,  50);
    lista = sllInsere(lista, -2);
    lista = sllInsere(lista,  80);

    printf("Lista:\n");
    sllImprime(lista);
    printf("\n");

    printf("Tamanho da lista: %d\n", sllComprimento(lista));
    printf("\n");

    sllBusca(lista, -15)->info = 500;
    printf("Lista depois de ter o info do no com valor -15 alterado:\n");
    sllImprime(lista);
    printf("\n");

    printf("Info no ultimo no da lista: %d", sllUltimo(lista)->info);

    return 0;
}