#include <iostream>
#include <vector>
#include <cmath>
#include <windows.h>
#include "Vetor.cpp"
#include "Busca.cpp"
using namespace std;

// https://stackoverflow.com/questions/1739259/how-to-use-queryperformancecounter
/** Use to init the clock */
#define TIMER_INIT \
    LARGE_INTEGER frequency; \
    LARGE_INTEGER t1,t2; \
    double elapsedTime; \
    QueryPerformanceFrequency(&frequency);

/** Use to start the performance timer */
#define TIMER_START QueryPerformanceCounter(&t1);

/** Use to stop the performance timer and output the result to the standard stream. Less verbose than \c TIMER_STOP_VERBOSE */
#define TIMER_STOP \
    QueryPerformanceCounter(&t2); \
    elapsedTime=(float)(t2.QuadPart-t1.QuadPart)/frequency.QuadPart; \
    std::wcout<<elapsedTime<<L" segundos ";
// ----------------------------------------------------------------------------//

int main()
{
    TIMER_INIT

    cout << "\nCriando vetores embaralhados e ordenados de tamanhos 10^3, 10^4, 10^5, 10^6 e 10^7." << endl;
    cout << "Escalei o tamanho dos vetores pois C++ eh muito veloz." << endl;

    TIMER_START
    vector<int> v0 = Vetor::cria_embaralhado((int)round(pow(10, 3)));
    vector<int> v1 = Vetor::cria_embaralhado((int)round(pow(10, 4)));
    vector<int> v2 = Vetor::cria_embaralhado((int)round(pow(10, 5)));
    vector<int> v3 = Vetor::cria_embaralhado((int)round(pow(10, 6)));
    vector<int> v4 = Vetor::cria_embaralhado((int)round(pow(10, 7)));

    vector<int> v5 = Vetor::cria_ordenado((int)round(pow(10, 3)));
    vector<int> v6 = Vetor::cria_ordenado((int)round(pow(10, 4)));
    vector<int> v7 = Vetor::cria_ordenado((int)round(pow(10, 5)));
    vector<int> v8 = Vetor::cria_ordenado((int)round(pow(10, 6)));
    vector<int> v9 = Vetor::cria_ordenado((int)round(pow(10, 7)));
    TIMER_STOP
    cout << "para criar os vetores" << "\n\n";

    TIMER_START
    cout << "Busca linear do numero 3 numa lista de tamanho 10^3" << endl;
    cout << "Indice: " + to_string(Busca::busca_linear(&v0, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca linear do numero 3 numa lista de tamanho 10^4" << endl;
    cout << "Indice: " + to_string(Busca::busca_linear(&v1, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca linear do numero 3 numa lista de tamanho 10^5" << endl;
    cout << "Indice: " + to_string(Busca::busca_linear(&v2, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca linear do numero 3 numa lista de tamanho 10^6" << endl;
    cout << "Indice: " + to_string(Busca::busca_linear(&v3, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca linear do numero 3 numa lista de tamanho 10^7" << endl;
    cout << "Indice: " + to_string(Busca::busca_linear(&v4, 3)) << endl;
    TIMER_STOP cout << "\n\n";


    TIMER_START
    cout << "Busca binaria do numero 3 numa lista de tamanho 10^3" << endl;
    cout << "Indice: " + to_string(Busca::busca_binaria(&v5, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca binaria do numero 3 numa lista de tamanho 10^4" << endl;
    cout << "Indice: " + to_string(Busca::busca_binaria(&v6, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca binaria do numero 3 numa lista de tamanho 10^5" << endl;
    cout << "Indice: " + to_string(Busca::busca_binaria(&v7, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca binaria do numero 3 numa lista de tamanho 10^6" << endl;
    cout << "Indice: " + to_string(Busca::busca_binaria(&v8, 3)) << endl;
    TIMER_STOP cout << "\n\n";
    
    TIMER_START
    cout << "Busca binaria do numero 3 numa lista de tamanho 10^7" << endl;
    cout << "Indice: " + to_string(Busca::busca_binaria(&v9, 3)) << endl;
    TIMER_STOP cout << "\n\n";


    cout << "Fim" << endl;

    return 0;
}