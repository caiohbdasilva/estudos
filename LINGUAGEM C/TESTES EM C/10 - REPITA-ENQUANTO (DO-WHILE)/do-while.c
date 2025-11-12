# include <stdio.h>

void limpar_entrada() {
    char c;
    while((c = getchar()) != '\n' && c != EOF);
}

int main (){

    double C, F;
    char resp;

    do
    {
        printf("Digite a temperatura em Celcius: ");
        scanf("%lf", &C);

        F = 9*C/5+32;

        printf("Equivalente em Farenheit: %.1lf\n", F);
        printf("Deseja repetir?");
        limpar_entrada();   
        scanf("%c", &resp);
    } while (resp=='s' || 'S');

    return 0;
    
}