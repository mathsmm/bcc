struct noLista 
{
    int info;
    struct noLista *prox;
};

typedef struct noLista NoLista;

NoLista *sllCria(void);
NoLista *sllInsere(NoLista *head, int v);
void     sllImprime(NoLista *head);
int      sllVazia(NoLista *head);
NoLista *sllBusca(NoLista *head, int v);
int      sllComprimento(NoLista *head);
NoLista *sllUltimo(NoLista *head);