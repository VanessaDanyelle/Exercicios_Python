"""
5) Faça um algoritmo estruturado que leia uma quantidade não determinada de
números positivos. Calcule a quantidade de números pares e ímpares,
a média de valores pares e a média geral dos números lidos.
 O número que encerrará a leitura será zero.
"""
if __name__ == '__main__':
    n = 1
    numpar = 0
    numgeral = 0
    qtnumpar = 0
    qtnumimp = 0

    while True:
        n = int(input('Digite um número '))
        if n == 0:
            break
        if n % 2 == 0:
            qtnumpar += 1
            numpar += n
        else:
            qtnumimp += 1
        numgeral += n

    print('Quantidade de números pares é {} e impares {}'.format(qtnumpar, qtnumimp))
    print('A média dos pares é {} e a média geral {}'.format(numpar/qtnumpar, numgeral/(qtnumpar+qtnumimp)))
