#include <stdio.h>
#include <locale.h>

int main(){

    setlocale(LC_ALL, "pt_BR.UTF-8");
    
    int idade;
    double salario;
    char nome[50] = "Maria Silva";
    char sexo;

    idade = 32;
    salario = 4560.33;
    sexo = 'F';

    printf("A funcionária %s, sexo %c, ganha R$ %.2lf e tem %d anos.\n", nome, sexo, salario, idade);

    return 0;
}