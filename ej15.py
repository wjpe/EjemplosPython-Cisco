#numero mayor modificado, utilizando while

numeroMayor = -99999999
contador = 0

while True:
    numero = int(input("Ingresa un numero o escribe -1 para finalizar el programa"))
    if numero == -1:
        break
    contador =1
    
    if numero > numeroMayor:
        numeroMayor = numero
    
if contador != 0:
    print("El numer mas grande es: ",numeroMayor)
else:
    print("No ha ingresado ningun numero")



'''
numeroMayor = -9999999
contador = 0

numero = int(input("Ingresa un numero o escribe -1 para terminar el programa"))

while numero != -1:
    if numero == -1:
        continue
    contador =1
    
    if numero > numeroMayor:
        numeroMayor = numero
    numero = int(input("Ingresa un numero o escribe -1 para terminar el programa"))
    
if contador:
    print("El numero mas grande es: ", numeroMayor)

else:
    print("No ha ingresado ningun numero")

'''