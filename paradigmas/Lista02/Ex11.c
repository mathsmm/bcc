#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//Função retirada de https://stackoverflow.com/questions/26620388/c-substrings-c-string-slicing
void slice(const char *str, char *result, size_t start, size_t end)
{
    strncpy(result, str + start, end - start);
}

int verifyCPF(char cpf[])
{
    int firstVerififer;
    int secondVerififer;

    int firstSum = 0;
    int i = 0;
    int j = 10;
    while (j >= 2)
    {
        firstSum = firstSum + atoi(cpf[i]) * j;
        i++;
        j--;
    }

    int rest = firstSum % 11;
    if (rest < 2)
    {
        firstVerififer = 0;
    }
    else
    {
        firstVerififer = 11 - rest;
    }

    char newCPF[12] = "";
    slice(cpf, newCPF, 0, 10);
    char strFirstVerifier[2];
    sprintf(strFirstVerifier, "%d", firstVerififer);
    newCPF[9] = strFirstVerifier;

    int secondSum = 0;
    i = 0;
    j = 11;
    while (j >= 2)
    {
        secondSum = secondSum + atoi(newCPF[i]) * j;
        i++;
        j--;
    }

    rest = secondSum % 11;
    if (rest < 2)
    {
        secondVerififer = 0;
    }
    else
    {
        secondVerififer = 11 - rest;
    }

    char strSecondVerifier[2];
    sprintf(strSecondVerifier, "%d", secondVerififer);

    strcat(newCPF, strSecondVerifier);

    if (newCPF == cpf)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int main()
{
    char cpf[12] = "20547311028";
    if (verifyCPF(cpf))
    {
        printf("CPF valido!");
    }
    else
    {
        printf("CPF nao valido!");
    }

    return 0;
}