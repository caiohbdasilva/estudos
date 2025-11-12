quantidade_intervalos = int(input("Por quantos intervalos de tempo o monitoramento será realizado? "))
contador = 0
limite_superior = 80
soma_total_usos = 0

while contador < quantidade_intervalos:
        uso_recurso = float(input(f"Uso do recurso no intervalo {contador + 1} (0-100): "))
        
        soma_total_usos += uso_recurso

        if uso_recurso > pico_uso:
            pico_uso = uso_recurso

        if uso_recurso > limite_superior:
            vezes_excedeu_limite += 1

        contador += 1

uso_medio = soma_total_usos / quantidade_intervalos

print(f"Uso médio do recurso: {uso_medio:.2f}%")
print(f"Pico de uso: {pico_uso:.2f}%")
print(f"O uso excedeu {limite_superior}% {vezes_excedeu_limite} vezes.")