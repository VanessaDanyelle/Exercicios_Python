'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.
'''

if __name__ == '__main__':
    nome = input('Nome do vendedor: ')
    salfixo = float(input('Salário: '))
    qtdevendas = float(input('Total de vendas efetuadas: '))
    bonus = float(qtdevendas * (15 / 100))
    total = salfixo + bonus
    print("TOTAL = R$ {:.2f}".format(total))
