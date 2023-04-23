''' 2) Desenvolver um algoritmo que leia a altura de 15 pessoas.
Este programa deverá calcular e mostrar :
a. A menor altura do grupo; b. A maior altura do grupo;
'''
if __name__ == '__main__':
    maioralt = 0
    menoralt = 0
    for c in range(1, 16):
        altura = float(input('Qual é a altura da pessoa {}? '.format(c)))
        if menoralt == 0:
            menoralt = altura
        if altura > maioralt:
            maioralt = altura
        if altura < menoralt:
            menoralt = altura

    print('A maior altura foi {} e a menor altura foi {}'.format(maioralt, menoralt))