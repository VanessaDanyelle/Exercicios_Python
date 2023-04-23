'''
1) Desenvolver um algoritmo que efetue a soma de todos os números ímpares
 que são múltiplos de três e que se encontram no
 conjunto dos números de 1 até 500.
'''
if __name__ == '__main__':
    soma = 0
    contador = 0
    for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c # mesma coisa que soma = soma + c
            contador += 1
            print(c)

    print('A soma de todos os {} valores é {} '.format(contador, soma))












