#! python

soma = 0
for x in range(1, 1000):
    if x % 3 == 0 or x % 5 == 0:
        print(f'{x}')
        soma += x

print(f'A soma total e: {soma} ')