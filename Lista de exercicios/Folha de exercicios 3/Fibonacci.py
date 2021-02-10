#! python

y = 0
z = 1
for _ in range(10):
    print(f'{y}')
    print(f'{z}')
    y = y + z
    z = y + z
