#include <stdio.h>
#include <locale.h>

int main(){

    setlocale(LC_ALL, "pt_BR.UTF-8");
    
    double x;
    x = 2.3456;

    printf("%.2lf\n", x);


    return 0;
}