'''
Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENÇA = (A * B - C * D).
'''

if __name__ == '__main__':
    n1 = int(input('Primeiro valor: '))
    n2 = int(input('Segundo valor: '))
    n3 = int(input('Terceiro valor: '))
    n4 = int(input('Quarto valor: '))
    diferenca = (n1 * n2) - (n3 * n4)
    print("DIFERENCA = {}".format(diferenca))
