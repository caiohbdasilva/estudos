###### BONUS PARA FUNCIONARIO

salario = float(input("Digite seu salário: "))
anos = int(input("Digite a quantidade de anos: "))

##### CÁLCULOS

bonus = 0.1

if anos >= 5:
    bonus = 0.2

salario += (salario*bonus)

print(f"O bônus será de {bonus:.2f}%")

print(f"O salário será de R$ {salario:.2f}")