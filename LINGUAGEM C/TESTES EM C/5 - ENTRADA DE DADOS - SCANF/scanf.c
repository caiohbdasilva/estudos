#include <stdio.h>
#include <string.h>

int main(){

    
    int idade;
    double salario, altura;
    char nome[50];

    printf("Digite o valor da idade: ");
// Para o scanf, antes da variável a ser lida, é necessário colocar o e comercial (&).
// Em uma explicação simples, o & busca a referência do endereço da variável na memória e adiciona o que foi 
//digitado pelo usuário.
    scanf("%d", &idade);

    printf("Digite o valor do salário: ");
    scanf("%lf", &salario);

    printf("Digite o valor da altura: ");
    scanf("%lf", &altura);

    printf("Digite o nome da pessoa: ");
// Para nomes, o scanf aceita apenas textos contíguos, ou seja, textos que não contenham espaços.
// Caso seja inserido pelo usuário texto com espaço, o scanf considerará apenas o texto antes do mesmo.
// Para textos com espaços utiliza-se o fgets.
// No caso de vetores, na linguagem C, não há a necessidade de se adicionar o '&'. Isso se deve pelo fato do
//vetor já ser uma referência dentro do próprio código, não havendo a necessidade de se buscar na memória.
    scanf("%s", nome[50]);

    printf("IDADE = %d\n", idade);
    printf("SALARIO = R$ %.2lf\n", salario);
    printf("ALTURA = %.2lf cm \n", altura);
    printf("NOME = %s\n", nome);
    
    return 0;
}