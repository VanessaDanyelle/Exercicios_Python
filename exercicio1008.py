'''
Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário.
A seguir, mostre o número e o salário do funcionário, com duas casas decimais.
'''

if __name__ == '__main__':
    numfunc = int(input('Número do funcionário: '))
    hrtrab = int(input('Horas trabalhadas: '))
    valorhr = float(input('Valor por hora: '))
    salario = float(hrtrab * valorhr)
    print("Número do funcionário = {}".format(numfunc))
    print("Salário = {:.2f}".format(salario))
