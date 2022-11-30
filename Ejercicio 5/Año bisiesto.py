año=int(input("Ingrese el año:  \n"))

def bisiesto(año):
    if año%4==0 and año%100!=0:
        return True
    elif año%100==0 and año%400==0:
        return True
    else:
        return False

print(bisiesto(año))