# Exercício 02

def dna_para_rna(dna):
    dna = dna.upper()
    rna = ""

    for nucleotideo in dna:
        if nucleotideo == "G":
            rna += "C"
        elif nucleotideo == "C":
            rna += "G"
        elif nucleotideo == "T":
            rna += "A"
        elif nucleotideo == "A":
            rna += "U"
        else:
            return "Sequência inválida: contém nucleotídeos desconhecidos."
    return rna


cadeia_dna = input("Digite a cadeia de DNA: (Sem vírgulas ou espaços) ")
resultado = dna_para_rna(cadeia_dna)
print("RNA complementar:", resultado)
