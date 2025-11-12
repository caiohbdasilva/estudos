############ CALCULO DE HIPOTENUSA #################

#Importando a biblioteca para cálculos futuros
import math

#Criando as variáveis e pedindo a entrada
cat1  = float(input("Digite o valor do primeiro cateto: "))
cat2 =  float(input("Digite o valor do segundo cateto: "))

#Fazendo o cálculo da hipotenusa
hip = math.sqrt((math.pow(cat1, 2))+(math.pow(cat2, 2)))

#Imprimindo o resultado
print(f"O resultado da hipotenusa é de {hip:.2f}")
