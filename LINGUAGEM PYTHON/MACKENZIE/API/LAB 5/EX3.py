valor_inicial = float(input("Informe o investimento inicial: "))
valor_final = float(input("Informe o investimento final: "))
dias = float(input("Informe a quantidade de dias investidos: "))

lucro = valor_final-valor_inicial

def calcular_ir(lucro, dias):
    if dias>720:
        ir = ((lucro/100) * 15)
    elif dias>360:
        ir = ((lucro/100) * 17.5)
    elif dias>180:
        ir = ((lucro/100) * 20)
    else:
        ir = ((lucro/100) * 22.5)
    return ir

ir = calcular_ir(lucro, dias)

print(f"O valor de IR a ser cobrado será de {ir:.2f}")