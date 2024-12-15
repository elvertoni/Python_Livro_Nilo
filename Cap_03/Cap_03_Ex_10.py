# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite seu salário atual: R$ "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

aumento = (salario + (salario*porcentagem_aumento/100))

print(f"O salário com aumento é: R$ {aumento:.2f}")