valor_investido = float(input("Informe o valor investido: "))
percentual_cdi = float(input("Informe o percentual CDI: "))
dias = int(input("Informe a quantidade de dias (considere um ano como 252 dias:) "))

def calcular_cdi(valor_investido, percentual_cdi, dias):
    rendimento = valor_investido*(1+(percentual_cdi/100)*(dias/252))
    return rendimento

rendimento = calcular_cdi(valor_investido, percentual_cdi, dias)

print(f"O retorno será de R$ {rendimento:.2f}")
if (rendimento>10000):
    print("Podem existir taxas melhores em investimentos privados.")


