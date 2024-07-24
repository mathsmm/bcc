#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int isPrime(int num)
{
    int i = 2;
    while (i < num)
    {
        if (num % i == 0)
            return 0;
        i++;
    }

    return 1;
}

int numbersQuantityUntilTwentyFivePrimes()
{
    int upper = 100;
    int lower = 1;
    int result = 0;
    int i = 0;
    while (i < 25)
    {
        int num = (rand() % (upper - lower + 1)) + lower;
        result++;

        if (isPrime(num))
        {
            i++;
        }
    }

    return result;
}

int main()
{
    srand(time(0));
    int num = numbersQuantityUntilTwentyFivePrimes();

    char response[100];
    sprintf(response, "%d", num);
    printf("Total de numeros gerados: ");
    printf("%s", response);

    return 0;

    //https://stackoverflow.com/questions/822323/how-to-generate-a-random-int-in-c/39475626#39475626
}