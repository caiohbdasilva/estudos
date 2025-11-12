valor_investido = float(input("Informe um valor investido: "))
rentabilidade = float(input("Informe a taxa de rentabilidade ao ano: "))
dias = int(input("Informe a quantidade de dias investidos: "))
prazo_dias = int(input("Informe a quantidade mínima de dias para resgate: "))

def verificar_resgate(valor_investido, rentabilidade, dias, prazo_dias):
    if dias>prazo_dias:
        retorno_desconto = (valor_investido + ((valor_investido/100)* rentabilidade)*(dias/252)) - ((valor_investido/100)*5)
    else:
        retorno = (valor_investido + ((valor_investido/100)* rentabilidade)*(dias/252))
    return retorno_desconto, retorno

retorno_desconto, retorno = verificar_resgate(valor_investido, rentabilidade, dias, prazo_dias)

if (retorno_desconto>retorno):
    print("Compensa resgatar.")
else:
    print("Compensa esperar.")