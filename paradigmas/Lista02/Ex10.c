#include <stdio.h>

int pertence(int num, int array[], int arrayLength)
{
    int i = 0;
    while (i < arrayLength)
    {
        if (num == array[i])
        {
            return 1;
        }
        i++;
    }

    return 0;
}

int main()
{
    int num = 2;
    int array[] = {0, 2, 4, 5, 6, 10, 11};
    size_t length = sizeof(array) / sizeof(array[0]);

    if (pertence(num, array, length))
    {
        printf("O numero pertence ao array!");
    }
    else
    {
        printf("O numero nao pertence ao array!");
    }

    return 0;
}