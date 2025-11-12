num = int(input("Digite um numero inteiro mior que 0, ou 0 para parar: "))

while num > 0:
  def inverter_digitos (num):
   num_str = str(num)
   num_invertido = num_str[::-1]
   return num_invertido
  print(inverter_digitos(num))
  def palindromo (num):
   num_str = str(num)
   num_invertido = num_str[::-1]
   if num_str == num_invertido:
     return "É palindromo"
   else:
     return "Não é palindromo"
  print(palindromo(num))
  num = int(input("Digite um numero: "))
  continue