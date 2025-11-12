valor_investido = float(input("Informe o valor investido: "))
percentual_cdi = float(input("Informe o percentual CDI: "))
dias = int(input("Informe a quantidade de dias (considere um ano como 252 dias:) "))
taxa_selic = float(input("Informe a taxa selic: "))

def calcular_cdi(valor_investido, percentual_cdi, dias):
    rendimento = valor_investido*(1+(percentual_cdi/100)*(dias/252))
    return rendimento

rendimento = calcular_cdi(valor_investido, percentual_cdi, dias)

def comparar_cdb_poupanca(valor_investido, dias, taxa_selic):
    cdb = ((rendimento/100)*110)*(dias/252)
    if taxa_selic > 8.5:
        poupanca = valor_investido + (((valor_investido/100)*8)*(dias/252))
    elif (dias > 30):
        poupanca = valor_investido + ((((valor_investido/100)*taxa_selic)*70)*(dias/252))
    else:
        poupanca = 0
    return cdb, poupanca

cdb, poupanca = comparar_cdb_poupanca(valor_investido, dias, taxa_selic)

print(f"O valor do CDB é de R${cdb:.2f}")
print(f"O valor da poupança é de R${poupanca:.2f}")

if(cdb>poupanca):
    print("O CDB é mais vantajoso.")
else:
    print("A poupança é a mais vantajosa.")

if(dias<30):
    print("A poupança não terá rendimento pois necessita de um aniversário mensal.")
