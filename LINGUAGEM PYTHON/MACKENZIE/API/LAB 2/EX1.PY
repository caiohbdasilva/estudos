##### CONVERSOR DE SEGUNDOS ##########

#Pedido de informação dos segundos
segundos = int(input("Informe o valor dos segundos: "))

#Estabelecendo limite para o segundo

while segundos>86399:
    segundos = int(input("Digite um valor abaixo de 86399: \n"))

#Criar as variáveis e executar os comandos
horas = int(segundos // 3600)
minutos = int(segundos-(horas*3600))//60
segundos = int(segundos-((minutos*60)+(horas*3600)))

#Imprimir os resultados codificados
print(horas,":",minutos,":",segundos)



