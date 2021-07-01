# bloques = int(input("Ingrese el número de bloques:"))

# #
# # Escribe tu código aquí.
# #
# altura = 0
# base = 0
# while bloques > 0:
#     if base == 0:
#         base = base +1
#         altura = altura +1
    
#     else:
#         if bloques > base:
#             base = base + 1
#             bloques = bloques - base
#             altura = altura+1
    
    
#     print ("base",base)

# print("La altura de la pirámide:", altura)

bloques = int(input("Ingrese el número de bloques:"))

capa_superior = 0
altura = 0

while bloques > 0:

    if capa_superior == 0:
        capa_superior += 1
        altura += 1
        bloques -= 1
    
    else:
        if bloques <= capa_superior:
            #altura = altura
            #print (altura)
            break
            #return 
        else:
            capa_superior += 1
            bloques = bloques - (altura + 1)
            print(f"capa superior{capa_superior}, bloque {bloques}")
            altura += 1
            

#
# Escribe tu código aquí.
#
print("La altura de la pirámide:", altura)
