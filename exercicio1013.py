'''
Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
'''

if __name__ == '__main__':
    A = int(input('Primeiro valor: '))
    B = int(input('Segundo valor: '))
    C = int(input('Terceiro valor: '))
    maior = max(A, B, C)
    print(maior, ' eh o maior')
