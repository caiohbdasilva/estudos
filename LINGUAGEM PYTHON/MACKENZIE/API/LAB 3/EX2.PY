###### CÁLCULO DE NOTAS

nota_peso2 = float(input("Insira a nota de peso 2: "))
nota_peso3 = float(input("Insira a nota de peso 3: "))
nota_peso5 = float(input("Insira a nota de peso 5: "))

###### CÀLCULO

nota_final = (((nota_peso2*2)+(nota_peso3*3)+(nota_peso5*5))/10)

resultado = "APROVADO"

if nota_final >= 6:
    resultado = "APROVADO"
else:
    resultado = "REPROVADO"

print(f"Sua nota será de {nota_final:.2f}")
print(resultado)