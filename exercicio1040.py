'''
Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno.
Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e mostre esta média acompanhada pela
mensagem "Media: ". Se esta média for maior ou igual a 7.0, imprima a mensagem "Aluno aprovado.". Se a média calculada
for inferior a 5.0, imprima a mensagem "Aluno reprovado.". Se a média calculada for um valor entre 5.0 e 6.9, inclusive
estas, o programa deve imprimir a mensagem "Aluno em exame.". No caso do aluno estar em exame, leia um valor correspondente
à nota do exame obtida pelo aluno. Imprima então a mensagem "Nota do exame: " acompanhada pela nota digitada. Recalcule a média
(some a pontuação do exame com a média anteriormente calculada e divida por 2). e imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais )
ou "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos). Para estes dois casos (aprovado ou reprovado após ter pego exame) apresente na última linha
uma mensagem "Media final: " seguido da média final para esse aluno.
'''

if __name__ == '__main__':
    n1 = float(input('Primeira Nota: '))
    n2 = float(input('Segunda Nota: '))
    n3 = float(input('Terceira Nota: '))
    n4 = float(input('Quarta Nota: '))

    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

    print("Media: {:.2f}".format(media))

    if media >= 7.0:
        print('Aluno aprovado.')
    elif media < 5:
        print("Aluno reprovado.")
    elif media >= 5 and media < 7:
        print("Aluno em exame.")

        n5 = float(input('Digite a nota da final: '))
        print("Nota do exame: {}".format(n5))
        novamedia = (media + n5) / 2

        if novamedia >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
            print('Media final: {}'.format(novamedia))