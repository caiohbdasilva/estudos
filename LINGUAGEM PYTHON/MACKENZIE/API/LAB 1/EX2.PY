import math

print("----------------Calculadora de área e raio---------------")

#Criando as variáveis
r = float(input("Informe o valor do raio: "))
pi = 3.1416

#Calculando a área e o perímetro
a = pi*math.pow(r,2)
p = 2*pi*r

#Imprimindo os valores da área e do perímetro
print(f"O valor da área é de {a:.2f} m2")
print(f"O valor do perímetro é de {p:.2f} mts")