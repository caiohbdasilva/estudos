lista = [3, 6, 1, 0, 9, 2, 7, 4, 5]
# 1 Descobrir o maior número da lista
maior = lista[0] # começa assumindo que o primeiro é o maior
for i in range(1, len(lista)): # percorre os índices de 1 até o final( começa em 1 pois o zero já assumimos em cima na varivel maior
 if lista[i] > maior:
     maior = lista[i] # atualiza o maior se achar número maior

# 2 Criar a lista de contagem (tudo com zero)
lista_Vazia = [0] * (maior + 1)

# 3 Contar quantas vezes cada número aparece
for i in range(len(lista)): # percorre todos os índices
 numero = lista[i] # pega o número correspondente
 lista_Vazia[numero] += 1 # soma 1 na posição do número

# 4 Criar a lista final ordenada
ordenada = []

# 5 Para cada número, repete ele quantas vezes apareceu
for numero in range(len(lista_Vazia)): # percorre os índices da contagem exemplo
 for j in range(lista_Vazia[numero]): # repete o número conforme a contagem
    ordenada.append(numero) # adiciona o número na lista ordenada

print("Lista Original: ", lista)
print("Lista Ordenada: ", ordenada)