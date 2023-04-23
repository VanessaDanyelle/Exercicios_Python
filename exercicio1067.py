'''
Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.
'''

if __name__ == '__main__':
    x = int(input('Digite o valor desejado: '))
    for i in range(1, x + 1):
        if i % 2 != 0:
            print(i)
