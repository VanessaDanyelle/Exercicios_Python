'''
Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou
"Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.
'''

if __name__ == '__main__':
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    if (a % b == 0) or (b % a == 0):
        print('são multiplos')
    else:
        print('Não são Multiplos')
