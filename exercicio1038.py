'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar

'''

if __name__ == '__main__':
    print('Código -- Especificação -- Preço')
    print('   1     Cachorro Quente   R$ 4.00')
    print('   2     X-Salada          R$ 4.50')
    print('   3     X-Bacon           R$ 5.00')
    print('   4     Torrada Simples   R$ 2.00')
    print('   5     Refrigerante      R$ 1.50')

    cod = int(input('Dígite o código: '))
    qty = int(input('Digite a quantidade: '))
    if cod == 1:
        total = qty * 4
    elif cod == 2:
        total = qty * 4.5
    elif cod == 3:
        total = qty * 5
    elif cod == 4:
        total = qty * 2
    elif cod == 5:
        total = qty * 1.5
    print("Total : R$  {:.2f}".format(total))
