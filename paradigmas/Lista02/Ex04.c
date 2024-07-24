#include <stdio.h>

int recFib(int range)
{
    if (range == 1)
    {
        return 1;
    }

    if (range == 0)
    {
        return 0;
    }

    return recFib(range - 1) + recFib(range - 2);
}

int main()
{
    int range = 10;
    int rangeFib = recFib(range);

    char response[100];
    sprintf(response, "%d", rangeFib);
    printf("%s", response);

    return 0;
}