//SOMENTE PARA INTEIROS POSITIVOS!
int recMult(int num1, int num2)
{
    if (num1 == 0)
    {
        return 0;
    }
    if (num1 == 1)
    {
        return num2;
    }
    return num2 + recMult(num1 - 1, num2);
}

int main()
{
    int num1 = 10;
    int num2 = 5;
    int mult = recMult(num1, num2);

    char response[100];
    printf("Multiplicacao entre os numeros: ");
    sprintf(response, "%d", mult);
    printf("%s", response);

    return 0;
}