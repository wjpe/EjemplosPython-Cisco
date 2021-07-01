#El programa nos dice cual es el numero mas grande entre tres numeros ingresados
#lee tres numeros
numero1 = int(input("Ingresa el primer numero"))
numero2 = int(input("Ingresa el segundo numero"))
numero3 = int(input("Ingresa el tercer numero"))

#asumimos temporalmente que el primer numero es el mas grande
#lo verificamos pronto

nmasGrande = numero1

#comprobamos si el segundo numero es mas grande que el mayor numero actual
#y actualiza el numero mas grande si es necesario

if numero2 > nmasGrande:
    nmasGrande = numero2

#comprobamos si el tercer numero es mas grande que el mayor numero actual
#y actualiza el numero mas grande si es necesario
if numero3 > nmasGrande:
    nmasGrande = numero3
    
#imprimir el resultado
print("El numero mas grande es: ", nmasGrande)
