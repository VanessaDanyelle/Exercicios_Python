'''
A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:

Salário                                 Percentual de Reajuste
0 - 400.00                                  15%
400.01 - 800.00                             12%
800.01 - 1200.00                            10%
1200.01 - 2000.00                           7%
Acima de 2000.00                            4%

Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

'''

if __name__ == '__main__':
    a = float(input('Digite seu salário: '))
    if 0 < a <= 400:
        rea = (((a * 15) / 100) + a)
        perc = 15
        print("Novo salario: {:.2f}".format(rea))
        print("Reajuste ganho: {:.2f}".format(rea - a))
        print("Em percentual: {} %".format(str(perc)))
    elif 400 < a <= 800:
        rea = ((a * 12) / 100 + a)
        perc = 12
        print(" Novo salario: {:.2f}".format(rea))
        print(" Reajuste ganho: {:.2f}".format(rea - a))
        print(" Em percentual: {} %".format(str(perc)))
    elif 800 < a <= 1200:
        rea = (((a * 10) / 100) + a)
        perc = 10
        print(" Novo salario: {:.2f}".format(rea))
        print(" Reajuste ganho: {:.2f}".format(rea - a))
        print(" Em percentual: {} %".format(str(perc)))
    elif 1200 < a <= 2000:
        rea = (((a * 7) / 100) + a)
        perc = 7
        print(" Novo salario: {:.2f}".format(rea))
        print(" Reajuste ganho: {:.2f}".format(rea - a))
        print(" Em percentual: {} %".format(str(perc)))
    else:
        rea = (((a * 4) / 100) + a)
        perc = 4
        print(" Novo salario: {:.2f}".format(rea))
        print(" Reajuste ganho: {:.2f}".format(rea - a))
        print(" Em percentual: {} %".format(str(perc)))
