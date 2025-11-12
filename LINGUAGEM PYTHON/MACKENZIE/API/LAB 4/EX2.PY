sim = 0
nao = 0
veredito = ""

telefone = (input("Telefonou para a vítima? (S/N)"))
if telefone == "S":
    sim = sim+1
else:
    nao = nao+1

local = (input("Esteve no local do crime? (S/N)"))
if local == "S":
    sim = sim+1
else:
    nao = nao+1
    
perto = (input("Mora perto da vítima? (S/N)"))
if perto == "S":
    sim = sim+1
else:
    nao = nao+1
    
divida = (input("Devia para a vítima? (S/N)"))
if divida == "S":
    sim = sim+1
else:
    nao = nao+1
    
trabalho = (input("Já trabalhou com a vítima?(S/N)"))
if trabalho == "S":
    sim = sim+1
else:
    nao = nao+1

if sim==2:
    veredito = "Suspeita"
elif sim==3 or sim==4:
    veredito = "Cúmplice"
elif sim==5:
    veredito = "Assassina"
else:
    veredito = "Inocente"

print("O veredito final é de ", veredito)


    
