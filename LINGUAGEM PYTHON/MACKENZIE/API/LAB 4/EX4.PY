peso = float(input("Informe o peso do pacote: "))
volume = float(input("Informe o volume do pacote: "))
km = float(input("Informe a distância da entrega: "))
transporte = ""
consumo = float(0.00)
combustivel = ""

if peso<=5 and volume<=0.05:
    transporte = "Moto"
    consumo = km*0.05
    combustivel = "Gasolina"
    custo = consumo*5.98
elif peso>5 and peso<=30 and volume>=0.05 and volume<=0.15:
    transporte = "Van"
    consumo = km*0.12
    combustivel = "Gasolina"
    custo = consumo*5.98
else:
    transporte = "Caminhão"
    consumo = km*0.3
    combustivel = "Diesel"
    custo = consumo*6.33
    
  
motorista = consumo*0.14

print("Tipo de veículo:", transporte)
print(f"Consumo de combustível: {consumo:.2f};")
print(f"O custo da viagem será de R$ {custo:.2f} com o combustível sendo {combustivel};")
print(f"O valor a ser pago aom motorista é de: R$ {motorista:.2f}.")
