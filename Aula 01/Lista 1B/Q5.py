E = float(input('Digite a espessura do papel: '))
V = int(input('Digite o número de vezes que ele foi dobrado: '))

espessura = (E * 2 ** V) / 1000

print(f"A espessura resultante é de {espessura:.0f}m")
