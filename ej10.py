#programa que lee una secuencia de numeros
#y cuenta cuantos numeros son pares y cuantos impares
# programa termina cuando se ingresa cero

numerosImpares = 0
numerosPares = 0

#lee el primer numero

numero = int(input("Introduzca un número o escriba 0 para detener"))

#0 Termina la ejecucion del programa
while numero != 0:
    #verificar si el numero es impar
    if numero % 2 == 1:
        #aumentar el contador de numeros impares
        numerosImpares += 1
        
    else:
        #aumentar el contador de numeros pares
        numerosPares += 1
    
    #lee el siguiente número
    numero = int(input("Introduce un número o escriba 0 para detener"))
    
#imprimir resultados
print("Números impares: ", numerosImpares)
print("Números pares", numerosPares)

