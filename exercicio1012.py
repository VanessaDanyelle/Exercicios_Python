'''
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
 a) a área do triângulo retângulo que tem A por base e C por altura.
 b) a área do círculo de raio C. (pi = 3.14159)
 c) a área do trapézio que tem A e B por bases e C por altura.
 d) a área do quadrado que tem lado B.
 e) a área do retângulo que tem lados A e B.
'''

if __name__ == '__main__':
    valor = input().split(" ")
    a, b, c = valor
    pi = 3.14159
    triangulo = (float(a) * float(c)) / 2
    circulo = pi * (float(c) * float(c))
    trapezio = float(c) * (float(a) + float(b)) / 2
    quadrado = float(b) * float(b)
    retangulo = float(a) * float(b)

    print('A área do triângulo é {}'.format(triangulo))
    print('A área do círculo é {}'.format(circulo))
    print('A área do trapézio é {}'.format(trapezio))
    print('A área do quadrado é {}'.format(quadrado))
    print('A área do retangulo é {}'.format(retangulo))
