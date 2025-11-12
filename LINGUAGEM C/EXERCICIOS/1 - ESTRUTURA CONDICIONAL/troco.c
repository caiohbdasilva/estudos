#include <stdio.h>

int main(){

    double unitario, recebido, troco;
    int qtde;

    printf("Preço unitário do produto: ");
    scanf("%lf", &unitario);

    printf("Quantidade comprada: ");
    scanf("%d", &qtde);

    printf("Dinheiro recebido: ");
    scanf("%lf", &recebido);

    troco = recebido-(unitario*qtde);

    printf("TROCO = R$ %.2lf", troco);
    
    return 0;
}