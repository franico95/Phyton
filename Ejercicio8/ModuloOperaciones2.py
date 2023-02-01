#Modulo operaciones 2

def suma(*args):
    resultado = 0
    for n in args:
        resultado += n
    return resultado


def resta(a, b):
    return a - b


def divide(a, b):
    return a / b


def multiplica(*args):
    resultado = 1
    for n in args:
        resultado *= n
    return resultado