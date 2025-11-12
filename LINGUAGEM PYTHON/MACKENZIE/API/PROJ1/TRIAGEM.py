############ SISTEMA DE TRIAGEM ###################

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

febre = float(input("Informe a medição de sua febre: "))
dor_de_cabeca = input("Está com dor de cabeça? (S/N)")

tosse = input("Está com tosse? (S/N)")


############ Variáveis aux. necessárias #############

intensidade_cabeca = int(0)
intensidade_tosse = ""

########### Tosse e Dor de cabeça (intensidade) ##################

if tosse == "S":
    intensidade_tosse = input("Informe se a tosse é seca (S) ou com catarro (C)")

if dor_de_cabeca == "S":
    intensidade_cabeca = int(input("Informe a intensidade da dor de cabeça, sendo 0 como mais leve e 10 como mais intenso: "))

############ Impressões e casos ###############

print("Nome: ", nome)
print("Idade: ", idade)

print(f"Febre: {febre:.2f}")
if febre == 39.0 or febre>39.0:
    print("Febre Alta (atenção urgente)")
elif febre > 37.5 or febre < 38.9:
    print("Febre Moderada (observação)")
else:
    print("Normal")

if intensidade_cabeca < 5:
    print("Dor de cabeça: Leve (autocuidado)")
elif intensidade_cabeca > 4 or intensidade_cabeca < 8:
    print("Dor de cabeça: Moderada (repouso)")
else:
    print("Dor de cabeça: Intensa (consulta médica)")

if tosse == "S":
    print("Necessita de Hidratação")
else:
    print("Possível infecção")

if intensidade_cabeca > 8 and intensidade_tosse == "S":
    print("Diagnóstico: Pode ser sinal de gripe, resfriado, Covid-19 ou outras infeções respiratórias, como a sinusite.")
elif intensidade_cabeca > 8 and intensidade_tosse == "C":
    print("Diagnóstico: Pode indicar condições como resfriado, gripe, sinusite, bronquite ou pneumonia.")
elif intensidade_cabeca >= 4 or intensidade_cabeca <= 8 and intensidade_tosse == "C":
    print("Diagnóstico: Pode indicar condições como resfriado, gripe.")
else:
    print("Problemas respiratórios.")

print("-----------------------------------------------------------------------------------------------------------------")
print("\n Advertimos que sempre é necessário ir a uma consulta médica!!!!")