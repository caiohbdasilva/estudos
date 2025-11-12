# 🎬 Sistema de Seleção de Assentos do CineMack
# Mostra 5 fileiras de 10 assentos (total 50)
# Ao escolher um assento, ele é marcado com "X"

def criar_assentos():
    # Cria uma lista com os números de 1 a 50
    assentos = []
    for i in range(1, 51):
        assentos.append(i)
    return assentos


def mostrar_assentos(assentos):
    print("Mapa de Assentos:")
    for i in range(0, 50, 10):  # mostra de 10 em 10
        for j in range(10):
            # formata cada número em 3 espaços (ou " X ")
            lugar = assentos[i + j]
            if lugar == "X":
                print(" X ", end=" ")
            else:
                # adiciona zeros à esquerda se quiser (opcional)
                print(f"{lugar:2}", end="  ")
        print()  # quebra de linha a cada fileira


def escolher_assento(assentos):
    while True:
        mostrar_assentos(assentos)
        try:
            escolha = int(input("Digite o número do assento que deseja (0 para sair): "))
        except ValueError:
            print("Digite um número válido!")
            continue

        if escolha == 0:
            print("Encerrando seleção de assentos.")
            break

        if escolha < 1 or escolha > 50:
            print("Assento inválido! Escolha um número entre 1 e 50.")
            continue

        if assentos[escolha - 1] == "X":
            print("Este assento já está ocupado! Escolha outro.")
            continue

        # Marca o assento como ocupado
        assentos[escolha - 1] = "X"
        print(f"Assento {escolha} reservado com sucesso!")


# ------------------------------
# Programa principal
# ------------------------------
def main():
    assentos = criar_assentos()
    escolher_assento(assentos)
    print("Estado final dos assentos:")
    mostrar_assentos(assentos)
    print("Obrigado por usar o sistema CineMack!")


# Executar o programa
main()
