#include <stdio.h>
#include <math.h>

int digits(int num)
{
    int result = 1;

    if (num == 0 || num == 1)
    {
        return result;
    }

    int aux;

    while (1)
    {
        aux = pow(10, result);

        if (num / aux == 0)
            break;

        result++;
    }

    return result;
}

int factorial(int num)
{
    int result = 1;

    while (num > 0)
    {
        result = result * num;
        num--;
    }

    return result;
}

int main()
{
    int num = 5;
    int numFact = factorial(num);

    int responseSize = digits(numFact);
    //char response[responseSize]; --> DÁ ERRO!
    char response[100];

    sprintf(response, "%d", numFact);
    printf("%s", response);

    return 0;
}