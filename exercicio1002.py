'''
 A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.

'''


if __name__ == '__main__':

    raio = float(input())
    area = 3.14159 * (raio * raio)
    print("A = {}".format(area))
