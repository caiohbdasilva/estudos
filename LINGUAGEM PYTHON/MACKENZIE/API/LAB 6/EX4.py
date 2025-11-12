def triangulo_numerico(numero):
 n = 1
 while n <= numero:
        texto = ""
        linha = 1
        while linha <= n:
            texto += str(linha) + " "
            linha += 1
        print(texto)
        n += 1

valor = int(input("Digite um número inteiro positivo: "))
triangulo_numerico(valor)