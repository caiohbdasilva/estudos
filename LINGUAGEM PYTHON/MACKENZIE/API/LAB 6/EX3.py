numero = int(input("Digite um número inteiro positivo: "))
algarismo = 0
soma_algarismos = 0
quantidade_pares = 0
quantidade_impares = 0

while numero > 0:
    algarismo = numero % 10
    soma_algarismos += algarismo
    numero = numero // 10

    if algarismo % 2 == 0:
        quantidade_pares += 1
    else:
        quantidade_impares += 1


print("Soma dos algarismos:", soma_algarismos)
print("Quantidade de algarismos pares:", quantidade_pares)
print("Quantidade de algarismos ímpares:", quantidade_impares)
