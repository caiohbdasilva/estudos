peso = float(input("Informe o peso do pacote: "))
volume = float(input("Informe o volume do pacote: "))
km = float(input("Informe a distância da entrega: "))
transporte = ""
consumo = float(0.00)

if peso<=5 and volume<=0.05:
    transporte = "Moto"
    consumo = km*0.05
elif peso>5 and peso<=30 and volume>=0.05 and volume<=0.15:
    transporte = "Van"
    consumo = km*0.12
else:
    transporte = "Caminhão"
    consumo = km*0.3
  

print("Tipo de veículo:", transporte)
print(f"Consumo de combustível: {consumo:.2f}")