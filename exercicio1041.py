'''
Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano.
A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
Se o ponto estiver na origem, escreva a mensagem “Origem”.
Se o ponto estiver sobre um dos eixos escreva “Eixo X” ou “Eixo Y”, conforme for a situação.
'''

if __name__ == '__main__':
    x = float(input('Digite o valor de X: '))
    y = float(input('Digite o valor de Y: '))

    if (x == 0) and (y == 0):
        print("Origem")
    elif(x == 0) and (y != 0):
        print("Eixo y")
    elif (x != 0) and (y == 0):
        print("Eixo x")
    elif (x > 0) and (y > 0):
        print("Q1")
    elif (x < 0) and (y > 0):
        print("Q2")
    elif (x < 0) and (y < 0):
        print("Q3")
    elif (x > 0) and (y < 0):
        print("Q4")
