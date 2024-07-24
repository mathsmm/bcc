#include <vector>
#include <iostream>
using namespace std;

class Busca
{
public:
    static int busca_linear(vector<int>* vet, int val)
    {
        int tam = vet->size();
        int i = 0;
        while (i < tam)
        {
            if ((*vet)[i] == val)
                return i;

            i++;
        }

        return -1;
    }

    static int busca_binaria(vector<int>* vet, int val)
    {
        int ini = 0;
        int fim = vet->size() - 1;
        int meio;
        while (ini <= fim)
        {
            meio = (ini + fim) / 2;

            if (val < (*vet)[meio])
            {
                fim = meio - 1;
            }
            else
            {
                if (val > (*vet)[meio])
                {
                    ini = meio + 1;
                }
                else
                {
                    return meio;
                }
            }
        }

        return -1;
    }
};