from time import localtime

#Se carga la hora local en las siguientes variables
hora = localtime().tm_hour
minutos = localtime().tm_min
segundos = localtime().tm_sec

if hora > 19:
    print('Es hora de ir a casa.')

else:
  print('Faltan %02d:%02d:%02d hs para salir.' % (18-hora, 59-minutos, 59-segundos))