g = int(input('Digite a quantidade de gotas que pingam por segundo: '))
v = int(input('Digite o volume de cada gota em mililitro: '))
d = int(input('Digite o número de dias de vazamento: '))

g = g * 60 ** 2 * 24 
volumeTotal = (g * v * d) / 1000

print(f"Foram desperdiçados {volumeTotal:.0f}L")
