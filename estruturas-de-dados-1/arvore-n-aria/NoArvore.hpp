#include <string>

class NoArvore
{
private:
    int info;
    NoArvore* prim;
    NoArvore* prox;

public:
    NoArvore(int info);

    void setInfo(int info);
    int  getInfo();

    void setPrim(NoArvore* prim);
    NoArvore* getPrim();

    void setProx(NoArvore* prox);
    NoArvore* getProx();

    std::string toString();
};