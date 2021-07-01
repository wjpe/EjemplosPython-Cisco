#Numero mayor de una serie de numeros digitados

#Almacenamos el numero mas grande actual aqui
numeroMayor = -999999999

#ingresamos el primer valor
numero = int(input("Introduzca un número o escriba -1 para detener:"))

#si el número ingresado no es igual a -1, continuamos
while numero != -1:
    # ¿Es el número más grande que el número más grande ?
    if numero > numeroMayor:
        #Si si, acutualiza el mayor númeroNúmero
        numeroMayor = numero

    #ingresa el siguiente número
    numero = int(input(" Introduzca un número o escriba -1 para detener:"))

#Imprimir el numero mas grande

print("El número mas grande es: ", numeroMayor)
