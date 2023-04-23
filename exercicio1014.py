'''
Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
'''

if __name__ == '__main__':
    x = int(input('Informe a distância total percorrida: '))
    y = float(input('Informe o total de combustível gasto em Litros: '))
    consumo_medio = x / y
    print("{:.2f} km/l".format(consumo_medio))
