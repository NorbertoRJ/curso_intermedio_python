from ast import comprehension


def run():
    # squares = []
    # for i in range (1,101):
    #     # Solo guardar los cuadrados de los números que no sean divisibles entre 3
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # list comprehension
    # squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    # print(squares)

    #Desafio
    # Crear, con un list comprehension, una lista de todos los múltiplos de 4
    # que a la vez también son múltiplos de 6 y de 9, hasta 5 dígitos

    elements = [i for i in range(1, 100000) if i % 36 == 0] #MCM
    #i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    print(elements)

if __name__ == '__main__':
    run()