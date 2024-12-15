# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.

metros = float(input("Digite um valor em metros para vê-lo em milímetros: "))
milimetros = metros * 1000

print(f"{metros:5.2f} metros convertidos para milímetros é {milimetros:5.2f} milímetros")