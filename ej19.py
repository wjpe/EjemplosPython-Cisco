bloques = int(input("Ingrese el número de bloques:"))

#
# Escribe tu código aquí.
#
altura = 0
while bloques > 0:
    altura = altura+1
    print ("al : ", altura)
    bloques = bloques -1
    

print("La altura de la pirámide:", altura)