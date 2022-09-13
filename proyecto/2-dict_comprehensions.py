def run():
    my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 != 0
    #         my_dict[i] = i**3

    # print(my_dict)

    #dicts comprehensions
    dict_1 = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(dict_1)

    # reto
    # crear, un dictionary comprehension, un diccionario cuyas llaves sean los 1000 primeros 
    # números naturales con raíces cuadradas como valores
    dict_reto = {i: i**0.5 for i in range(1, 1001)}
    print(dict_reto)


if __name__ == '__main__':
    run()