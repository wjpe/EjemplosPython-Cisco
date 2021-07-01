numeroSecreto = 777

print(
"""
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

numeroUsuario = int(input("Digita un numero "))
salida = 1

while salida !=0:
    if numeroUsuario != numeroSecreto:
        print("¡Ja, Ja, Ja!, ¡Estas atrapado en mi ciclo!")
        numeroUsuario = int(input("Digita otro numero numero "))
    else:
        salida = 0
        print("Bien hecho muggle eres libre ahora")