codigo = int(input("DIgite o código do produto: "))
classificacao = ""
if codigo == 1:
    classificacao = "Alimento não-perecível"
elif codigo == 2 or codigo==3 or codigo == 4:
    classificacao = "Alimento perecível"
elif codigo == 5 or codigo == 6:
    classificacao = "Vestuário"
elif codigo == 7:
    classificacao = "Higiene Pessoal"
elif codigo == 8 or codigo==9 or codigo == 10:
    classificacao = "Utensílios Domésticos"
else:
    classificacao = "Categoria Inválida."

print("A categoria do seu produto é: ", classificacao)

