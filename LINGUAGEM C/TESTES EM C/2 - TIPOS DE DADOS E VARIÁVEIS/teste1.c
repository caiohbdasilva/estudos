#include <stdio.h>
#include <string.h>
#include <locale.h>

int main(){

    setlocale(LC_ALL, "pt_BR.UTF-8");
    
    int idade;
    double salario, altura;
    char genero;
    char nome[50] = "Maria Silva";

    idade = 20;
    salario = 5800.5;
    altura = 1.63;
    genero = 'F';
    
    printf("IDADE = %d\n", idade);
    printf("SALARIO = R$ %.2lf\n", salario);
    printf("ALTURA = %.2lf cm \n", altura);
    printf("GENERO = %c\n", genero);
    printf("NOME = %s\n", nome);

    return 0;
}