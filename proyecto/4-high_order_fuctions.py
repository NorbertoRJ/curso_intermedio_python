def saludo(func):
    func()


def hola():
    print("Hola")


def adios():
    print("Adios")


saludo(hola)
saludo(adios)


#filter, map, reduce

#list comprehensions
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd = [i for i in my_list if i % 2 != 0]
print(odd)

# filter
odd = list(filter(lambda x: x % 2 != 0, my_list)) # filter retorna un iterador, por eso se asigna a un list para obtener el resultado 
print(odd)

# -------------------------------------

#list comprehensions
my_list = [1, 2, 3, 4, 5]
squares = [1**2 for i in my_list]
print(squares)

# map
squares = list(map(lambda x:x**2, my_list))
print(squares)

# -------------------------------------
# for 
my_list = [2, 2, 2, 2, 2]
all_multiplied = 1
for i in my_list:
    all_multiplied = all_multiplied * i
print(all_multiplied)

#reduce
from functools import reduce
my_list = [2, 2, 2, 2, 2]
all_multiplied = reduce(lambda a, b: a * b, my_list)
# corrida de escritorio
# 1 - lamda 2, 2: 2 * 2, []
# 2 - lamda 4, 2: 4 * 2, []
# 3 - lamda 8, 2: 8 * 2, []
# 4 - lamda 16, 2: 16 * 2, []
#salida : 32
print(all_multiplied)


