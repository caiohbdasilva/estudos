############## PESOS DOS PEIXES

peso = float(input("Informe o peso dos peixes: "))

multa = float(4)

if peso>50:
    multa = (peso-50)*4
    print(f"Multa = R$ {multa:.2f}")
else:
    print("Dentro do regulamento.")