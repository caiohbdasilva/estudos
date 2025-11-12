import math

def calcular_raizes(a,b,c):
    delta = math.pow(b,2) - 4*a*c
    x1 = (-b + math.sqrt(delta))/(2*a)
    x2 = (-b - math.sqrt(delta))/(2*a)
    print("Raízes:")
    print("X1 =", x1)
    print("X2 =", x2)

num1 = int(input("Digite o valor de a: "))
num2 = int(input("Digite o valor de b: "))
num3 = int(input("Digite o valor de c: "))

calcular_raizes(num1, num2, num3)