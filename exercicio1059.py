'''
Faça um programa que mostre os números pares entre 1 e 100, inclusive.
'''

if __name__ == '__main__':
    for p in range(1, 101):
        if p % 2 == 0:
            print(p)
