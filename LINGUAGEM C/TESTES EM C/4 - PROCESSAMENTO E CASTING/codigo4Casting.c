#include <stdio.h>

int main(){

    int a, b;
    double resultado;

    a = 5;
    b = 2;

// Executaremos a conta sem o Casting (conversão) e verifique que não haverá casas decimais na
//resposta.
// Isso ocorre pois, uma vez que é dividido dois números INT, a linguagem interpreta que 
//somente os números inteiros precisam ser divididos, desconsiderando a parte fracionária.
    resultado = a/b;
    printf("Resultado sem Casting: %1lf\n", resultado);

// O Casting entra para conversão de tipos de dados.
// Ex.: Para pegarmos a sobra da divisão a seguir, temos que converter alguma das variáveis 
//para double.
// Assim, o sistema entende que é necessário considerar as casas decimais, mesmo o resultado 
//já sendo double.
    resultado = (double) a/b;
    printf("Resultado com Casting: %1lf\n", resultado);

    return 0;
}