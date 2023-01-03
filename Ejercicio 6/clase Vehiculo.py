class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
    def __str__(self):
        return "El vehiculo de color {} , tiene {} ruedas y {} puertas".format(self.color, self.ruedas,self.puertas)

class Coche(Vehiculo):
    def __init__(self,color,ruedas,puerta, velocidad, cilindrada):
        Vehiculo.__init__(self,color,ruedas,puerta)
        self.cilindrada = cilindrada
        self.velocidad = velocidad
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} cilindrada y velocidad de {} ".format(self.cilindrada, self.velocidad)

mi_Vehiculo = Vehiculo('rojo', 'cuatro', 'cinco')
print(mi_Vehiculo)
mi_Coche =Coche('verde','cuatro','cinco','180', 'cuatro')
print(mi_Coche)