#! python

for i in range(1, 10):
    if (i % 2) == 0 and (i % 3) == 0:
        print(str(i) + ' oi tchau')
    elif (i % 2) == 0:
        print(str(i) + ' oi')
    elif (i % 3) == 0:
        print(str(i) + ' tchau')
    else:
        print(str(i))