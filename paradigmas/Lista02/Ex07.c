int dividersSum(int num)
{
    int result = 1;
    int i = 2;
    int j = num / 2;
        while (i <= j)
        {
            if (num % i == 0)
            {
                result = result + i;
            }
            i++;
        }

    return result;
}

int perfect(int num)
{
    if (dividersSum(num) == num)
    {
        return 1;
    }
    return 0;
}

int main()
{
    int num = 6;
    if (perfect(num))
    {
        printf("Numero eh perfeito!");
    }
    else
    {
        printf("Numero nao eh perfeito!");
    }

    return 0;
}