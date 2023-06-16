a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))

delta = (b ** 2) - 4 * a * c

x2 = (-b + delta ** (1 / 2)) / (2 * a)

print(f"O valor de x2 é {x2}")