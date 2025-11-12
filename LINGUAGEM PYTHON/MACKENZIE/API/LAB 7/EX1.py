senha = 1234
entrada = int(input("digite a senha:"))
while entrada != senha:
  print("Acesso negado")
  entrada = int(input("digite a senha:"))
if  senha == 1234:
  print("Acesso Permitido! Bem-vindo(a)")