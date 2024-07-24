#include <stdio.h>

int rec_factorial(int num)
{
    if (num ==1 || num == 0)
    {
        return 1;
    }

    return num * rec_factorial(num - 1);
}

int main()
{
    int num = -1;
    int numFact = rec_factorial(num);

    char response[100];
    sprintf(response, "%d", numFact);
    printf("%s", response);

    return 0;
}