#Clase
class Alumno():
    def inicializar(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
#Funciones
    def imprimir(self):
        print("Nombre: ",self.nombre)
        print("Nota: ",self.nota)
    
    def resultado(self):
        if self.nota < 5:
            print("El alumno ha desaprobado")
        else:
            print("El alumno ha aprobado")
#Bloque principal
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Andrea",8)
alumno2.inicializar("Ernesto",2)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()