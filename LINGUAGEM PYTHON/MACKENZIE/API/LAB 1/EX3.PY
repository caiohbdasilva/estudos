
#Criando as variáveis
m2 = float(input("Informe a quantidade de m2 que será printado: "))

#Executar cálculos para obter as informações
l = m2/3
qtdelatas = int(l/18)

if l<1:
    l=1

if qtdelatas<1:
    qtdelatas=1

custo = qtdelatas*80




#Impressão de informações
print("-----------------------------------------------------------------------")
print("Segue abaixo as informações:")
print("")
print(f"Qtde de litros necessárias: {l:.2f}")
print(f"Qtde de latas necessárias: {qtdelatas}")
print(f"Preço total da compra: R$ {custo:.2f}")