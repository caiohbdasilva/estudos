#include <stdio.h>

int main(){

    double a;
    int b;

    a = 5.0;
    b = (int)a;
// Na linguagem C não há a necessidade de fazer essa conversão de tipos de variáveis. Porém 
//pode haver a necessidade em outras linguagens.

    printf("%d\n", b);

    return 0;
}