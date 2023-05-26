
soma = 0

for i in range(1, 4):
    nota = float(input(f'Informe a sua nota {i}:'))
    soma += nota
    média = soma / 3
print(f'Sua média é {média:.2f}')
