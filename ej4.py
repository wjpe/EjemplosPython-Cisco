#Este programa
#Ingresa dos numeros y nos dice cual es el mas grande


#lee dos numeros
numero1 = int(input("Ingresa el primer numero"))
numero2 = int(input("Ingresa el segundo numero"))

#elegir el numero mas grande

if numero1 > numero2:
    nmasGrande = numero1
else:
    nmasGrande = numero2

#imprimir el resultado

print("El Numero mas grande es:", nmasGrande)
