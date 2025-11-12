# Exercício 01

def ler_notas():
    notas = []
    nota = float(input("Digite uma nota (-1 para encerrar): "))

    while nota != -1:
        notas.append(nota)
        nota = float(input("Digite uma nota (-1 para encerrar): "))
    return notas


def processar_notas(notas):
    print(f"Quantidade de notas lidas: {len(notas)}")


    print("Notas na ordem informada:")
    for n in notas:
        print(n)


    print("\nNotas na ordem inversa:")
    for n in reversed(notas):
        print(n)


    soma = sum(notas)
    print(f"\nSoma das notas: {soma:.2f}")


    media = soma / len(notas) if notas else 0
    print(f"Média das notas: {media:.2f}")


    acima_media = sum(1 for n in notas if n > media)
    print(f"Quantidade de notas acima da média: {acima_media}")

if __name__ =="__main__":
    processar_notas(ler_notas())