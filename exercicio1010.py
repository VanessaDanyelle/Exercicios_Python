'''
Neste problema, deve-se ler o código de uma peça 1, o número de peças 1,
o valor unitário de cada peça 1, o código de uma peça 2, o número de peças 2 e o valor unitário de cada peça 2.
Após, calcule e mostre o valor a ser pago.
'''

if __name__ == '__main__':
    linha1 = input().split(" ")
    linha2 = input().split(" ")
    cod1, qtde1, valor1 = linha1
    cod2, qtde2, valor2 = linha2
    total = (int(qtde1) * float(valor1)) + (int(qtde2) * float(valor2))
    print("VALOR A PAGAR: R$ {:.2f}".format(total))
