'''
8) Escreva um algoritmo que leia um valor inicial A e uma razão R e
imprima uma seqüência em P.A. contendo 10 valores.
'''
if __name__ == '__main__':
    primeiro = int(input('Primeiro termo: '))
    razao = int(input('Razão: '))
    for c in range(primeiro, 10, razao):
        print('{}'.format(c), end=' => ')
    print('FIM')