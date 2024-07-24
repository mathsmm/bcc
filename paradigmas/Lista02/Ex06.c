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

int friends(int num1, int num2)
{
    if ((num1 == dividersSum(num2)) && (num2 == dividersSum(num1)))
    {
        return 1;
    }
    return 0;
}

int main()
{
    int num1 = 220;
    int num2 = 284;
    if (friends(num1, num2))
    {
        printf("Sao amigos!");
    }
    else
    {
        printf("Nao sao amigos!");
    }

    return 0;
}