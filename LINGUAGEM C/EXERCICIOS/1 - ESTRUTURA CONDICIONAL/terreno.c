#include <stdio.h>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "pt_BR.UTF-8");

    double larg, comp, m2, precoarea, precoterreno;

    printf("Digite a largura do terreno: ");
    scanf("%lf", &larg);

    printf("Digite o comprimento do terreno: ");
    scanf("%lf", &comp);

    printf("Digite o valor do m²: ");
    scanf("%lf", &precoarea);

    m2 = larg*comp;
    precoterreno = precoarea * m2;

    printf("Área do terreno: %.2lf m²\n", m2);
    printf("Preço do terreno: R$ %.2lf\n", precoterreno);

    return 0;
}