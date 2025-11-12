#include <stdio.h>
//Para utilização do FGETS e STRTOK é imprescindível a inclusão da biblioteca string.h
#include <string.h>


// Quando o mesmo código é usado diversas vezes, pode-se utilizar um padrão, o que é chanado de 'função'*
void limpar_entrada() {
 char c;
 while ((c = getchar()) != '\n' && c != EOF) {}
}

void ler_texto(char *buffer, int length) {
 fgets(buffer, length, stdin);
 strtok(buffer, "\n");
} 


int main(){

    
    int idade1, idade2;
    char nome1[50],nome2[50];

    printf("Digite o valor da idade 1: ");
    scanf("%d", &idade1);
// Após a leitura, o FGETS entende o ENTER usado para a confirmação como uma quebra de linha. Como o conceito do FGETS 
//é ler os caracteres até a quebra de linha, ele entende que já foi informado a entrada. Para evitar, devemos usar a
//'limpeza de buffer de entrada', presente na função* 'limpar_entrada()' (ler linha 6), antes de executar o FGETS, assim 
//não ocorerá essa associação.

    printf("Digite o nome da pessoa 1: ");
// FGETS é usado para leitura de caracteres até a quebra de linha.(Isso será importante para entender o
//funcionamento da linha 18).
// No FGETS é necessário adicionar o nome da variável, a quantidade pré-estabelecida e de onde a informação virá.
// STDIN é a abreviação de 'Standard Input' = 'Entrada Padrão'
    limpar_entrada();
    fgets(nome1, 50, stdin);
// O FGETS guarda tudo até a quebra de linha, inclusive a própria quebra. Caso não queira guardá-la, pode-se usar o
//comando STRTOK
    strtok(nome1, "\n");

    printf("Digite o valor da idade 2: ");
    scanf("%d", &idade2);

    printf("Digite o nome da pessoa 2: ");
    limpar_entrada();
//Para evitar repetição, podemos deixar o FGETS e o STRTOK em uma função no void e chamá-la quando necessário apenas como
//'ler_texto'
    ler_texto(nome2, 50);

    printf("IDADE 1 = %d\n", idade1);
    printf("NOME 1 = %s\n", nome1);
    printf("IDADE 2 = %d\n", idade1);
    printf("NOME 2 = %s\n", nome1);
    
    return 0;
}