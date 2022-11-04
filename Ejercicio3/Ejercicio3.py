def imc(estatura, peso):

    return peso / estatura**2

peso = float(input('Escriba su peso (KG): '))
estatura = float(input('Escriba su estatura (M):'))

indice = imc(estatura, peso)

print('Su IMC es: {}'.format(indice))


