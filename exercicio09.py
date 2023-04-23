'''
9) Escreva um algoritmo que leia um valor inicial A e uma razão R
e imprima uma seqüência em P.G. contendo 10 valores.
'''

if __name__ == '__main__':
    a = int(input('Digite um valor inicial:'))
    r = int(input('Digite a razão '))
    pa = a
    for c in range(10):
        print('{} => '.format(pa), end='')
        pa *= r
    print('ACABOU')