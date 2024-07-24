class NoArvoreBinaria
{
private:
    int info;
    NoArvoreBinaria* sae;
    NoArvoreBinaria* sad;
    
public:
    NoArvoreBinaria(int info);
    NoArvoreBinaria(int info, NoArvoreBinaria* esq, NoArvoreBinaria* dir);
    
    int  getInfo();
    void setInfo(int info);
    
    NoArvoreBinaria* getSae();
    void setSae(NoArvoreBinaria* esq);
    
    NoArvoreBinaria* getSad();
    void setSad(NoArvoreBinaria* dir);
};