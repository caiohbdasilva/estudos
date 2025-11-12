valor_compra = float(input("Informe o valor da compra: "))
valor_recebido = float(input("Informe a cédula recebida do cliente: "))
valor_faltante = valor_compra-valor_recebido

while valor_faltante > 0:
    novo_recebido = float(input(f"Informe mais uma cédula, faltam R$ {valor_faltante:.2f} \n "))
    valor_recebido = valor_recebido+novo_recebido
    valor_faltante = valor_compra-valor_recebido

if valor_faltante< 0:
    print(f"Valor pago! O seu troco é de R$ {(valor_faltante*-1):.2f}")
else:
    print("Valor pago! Sem troco!")