#año bisiesto
#año dentro del calendario gregoriano

año = int(input("Introduzca un año:"))

#
# Coloca tu código aquí.
#


if año < 1582:
    print("No dentro del periodo del calendario gregoriano")

elif (año%4) != 0:
    print("es año comun")
elif (año%100) !=0 :
    print("El año es bisiesto")
elif (año %400) != 0:
    print("es un año comun")

else:
    print("Es un año bisiesto")
