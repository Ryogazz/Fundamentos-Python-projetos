#! python

ip = int(input('Digite o numero do IP: '))

if ip >= 0 and ip <= 127:
    print('Ip classe A')
elif ip >= 128 and ip <= 191:
    print('Ip classe B')
elif ip >= 192 and ip <= 223:
    print('Ip classe C')
elif ip >= 224 and ip <= 239:
    print('Ip classe D')
else:
    print('Ip classe D')