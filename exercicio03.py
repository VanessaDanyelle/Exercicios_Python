'''
3) Desenvolver um algoritmo que leia um número não determinado de
valores e calcule e escreva a média aritmética dos valores lidos,
a quantidade de valores positivos,
a quantidade de valores negativos e o percentual de
valores negativos e positivos.
'''

if __name__ == '__main__':

    qtpositivo = 0
    qtnegativo = 0
    somapos = 0
    somaneg = 0
    qtnegepos = 0
    somanegepos = 0

    while True:
        num = float(input('Digite um número: '))
        if num > 0:
            qtpositivo += 1
            somapos += num
        else:
            qtnegativo += 1
            somaneg += num
        qtnegepos += 1
        somanegepos += num
        x = input('Deseja continuar? [S/N] ')
        if x in 'nN':
            break

    print('A média aritmética é {}'.format(somanegepos/qtnegepos))
    print('A quantidade de positivos é {} e de negativos {}'.format(qtpositivo, qtnegativo))
    print('O percentual de positivo é {:.2f}% e o de negativo {:.2f}%'.format(qtpositivo*100/qtnegepos, qtnegativo*100/qtnegepos))
