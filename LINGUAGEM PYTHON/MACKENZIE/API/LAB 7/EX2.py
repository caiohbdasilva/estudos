soma_notas = 0
total_notas = 0
nota = float(input("Digite a nota do aluno (ou -1 para parar): "))
media = 0

if nota == -1:
   print("Programa encerrado")

while nota  != -1:
   soma_notas += nota
   total_notas += 1
   media = soma_notas / total_notas
   nota = float(input("Digite a nota do aluno (ou -1 para parar): "))
print  ("A media das notas é: ", media)