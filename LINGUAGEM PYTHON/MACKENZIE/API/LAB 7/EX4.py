menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))
saida = "Programa encerrado"

while menu < 8:
   if menu == 1:
      num = int(input("Digite um numero para calcular o fatorial: "))
      def fatorial (num):
         if num == 1:
            return 1
         elif num == 0:
            return 1
         ret = 1
         while num > 1:
            ret *= num
            num -= 1
         return ret
      print(fatorial(num))
      menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))
      continue

   elif menu == 2:
     num = int(input("Digite um numero para calcular a sequencia de fibonacci: "))
     def fibonacci (num):
       if num == 1:
         return 1
       elif num == 0:
         return 0
       else:
         return fibonacci (num - 1) + fibonacci (num - 2)
     print(fibonacci (num))
     menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))
     continue

   elif menu == 3:
       num = int(input("Digite um numero para inverter os digitos: "))
       def inverter_digitos (num):
         num_str = str(num)
         num_invertido = num_str[::-1]
         return num_invertido
       print(inverter_digitos(num))
       menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))

   elif menu == 4:
       num = int(input("Digite um numero para calcular a progressao geometrica: "))
       def progressao_geometrica (num):
         if num == 1:
           return 1
         elif num == 0:
           return 0
         else:
           return progressao_geometrica (num - 1) * 2
       print(progressao_geometrica(num))
       menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))
       continue

   elif menu == 5:
       num = int(input("Digite um numero para verificar se é palindromo: "))
       def palindromo (num):
         num_str = str(num)
         num_invertido = num_str[::-1]
         if num_str == num_invertido:
           return "É palindromo"
         else:
           return "Não é palindromo"
       print(palindromo(num))
       menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))
       continue

   elif menu == 6:
        num = int(input("Digite um numero para calcular a soma dos digitos: "))
        def soma_digitos (num):
          soma = 0
          while num > 0:
            soma += num % 10
            num = num // 10
          return soma
        print(soma_digitos(num))
        menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))
        continue

   elif  menu == 7:
       print(saida)
       break

while menu >= 8:
   print("Opção inválida")
   menu = int(input("Escolha uma opção: \n 1 - Fatorial \n 2 - Fibonacci \n 3 - Inverter digitos \n 4 - Progressao geometrica \n 5 - Palindromo numerico \n 6 - Soma de digitos \n 7 - Sair \n R:"))