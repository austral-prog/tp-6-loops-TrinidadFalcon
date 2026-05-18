# Replace the "ANSWER HERE" for your answer

def power(base, exp):
    """
    Retorna base elevado a exp usando un bucle for.
    exp es siempre >= 0.

    Ejemplo: power(2, 3) -> 8  (2*2*2)
    """

    potencia= 1
    for i in range(exp):
       potencia *= base
    return potencia

def sum_of_powers(base, max_exp):

    suma = 0
    for i in range(0,max_exp):
        suma += base**i
    return suma



