'''
7) Escrever um algoritmo que leia um valor para uma variável N de 1 a 10 e
calcule a tabuada de N. Mostre a tabuada na forma: 0 x N = 0, 1 x N = 1N,
2 x N = 2N, ..., 10 x N = 10N.
'''
if __name__ == '__main__':
    n = int(input('Você deseja a tabuada de qual número? '))
    for c in range(10):
        print('{} x {} = {}'.format(n, c, n*c))
