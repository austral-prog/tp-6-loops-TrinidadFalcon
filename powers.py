def power(base, exp):


    resultado = 1

    for i in range(exp):
        resultado *= base

    return resultado


def sum_of_powers(base, max_exp):


    suma = 0

    for i in range(max_exp + 1):
        suma += power(base, i)

    return suma

