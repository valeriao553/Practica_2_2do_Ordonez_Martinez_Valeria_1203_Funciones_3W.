#Factorial ejercicio 3
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Ejercicio 2 Factorial")
print(" ")
 #Solicitar al usuario que ingrese un número natural
print("Ingrese un número natural: ")
num = int(input())  # Convertir la entrada a un entero

# Indicar la variable fact
fact = 1

# Crear un bucle para calcular el factorial de 1 hasta num
for i in range(1, num + 1):
    # Multiplicar fact por i para ir acumulando los números
    fact *= i

# Imprimir el resultado final del factorial
print("El factorial de", num, "es:", fact)
print (" ")
