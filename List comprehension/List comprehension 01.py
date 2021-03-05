#! python

dobro = [i * 2 for i in range(10)]

print(dobro)


#///////////////////////////////
# sem  comprehension

dobros = []

for i in range(10):
    dobros.append(i * 2)
print(dobros)