###### Qtde de notas

valor = float(input("Digite o valor recebido: "))

n100 = int(valor/100)
resto = valor%100

n50 = int(resto/50)
resto = resto%50

n20 = int(resto/20)
resto = resto%20

n10 = int(resto/10)
resto = resto%10

n5 = int(resto/5)
resto = resto%5

n2 = 0
n1 = 0

if resto%2 == 0:
    n2= int(resto/2)
else:
    n2 = int(resto/2)
    resto = resto%2
    n1 = int(resto)

print("Quantidade de notas:")
print("Notas de 100: ", n100)
print("Notas de 50: ", n50)
print("Notas de 20: ", n20)
print("Notas de 10: ", n10)
print("Notas de 5: ", n5)
print("Notas de 2: ", n2)
print("Notas de 1: ", n1)

