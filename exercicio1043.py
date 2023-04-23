'''
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
Perimetro = XX.X
Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
Area = XX.X
'''

if __name__ == '__main__':
    a = float(input('Primeiro valor: '))
    b = float(input('Segundo valor: '))
    c = float(input('Terceiro valor: '))
    perimetro = a + b + c
    area = (a + b) * c / 2
    if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
        print("Perimetro  = {:.1f}".format(perimetro))
    else:
        print("Area = {:.1f}".format(area))
