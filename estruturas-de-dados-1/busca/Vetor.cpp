#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <random>
#include <time.h>
using namespace std;

class Vetor
{
public:
    static vector<int> cria_ordenado(int n)
    {
        vector<int> v;
        int i = 1;
        while (i <= n)
            v.push_back(i++);

        return v;
    }

    static vector<int> cria_embaralhado(int n)
    {
        vector<int> v;
        while (n > 0)
            v.push_back(n--);

        auto rng = default_random_engine(time(NULL));
        shuffle(begin(v), end(v), rng);

        return v;
    }

    static string to_str(vector<int> v)
    {
        string s = "[" + std::to_string(v[0]);
        int fim = v.size() - 1;
        int i = 1;
        while (i <= fim)
        {
            s += ", " + std::to_string(v[i]);
            i++;
        }

        return s + "]";
    }
};