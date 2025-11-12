#include <stdio.h>
#include <locale.h>
#include <math.h>

int main(){
    setlocale(LC_ALL, "pt_BR.UTF-8");

    double b,h,a,p,d;

    printf("Base do retângulo: ");
    scanf("%lf", &b);

    printf("ALtura do retângulo: ");
    scanf("%lf", &h);

    a = b*h;
    p = (2*b)+(2*h);
    d = sqrt((b*b)+(h*h));

    printf("ÁREA = %.4lf\n", a);
    printf("PERÍMETRO = %.4lf\n", p);
    printf("DIAGONAL = %.4lf\n",d);

    return 0;
}