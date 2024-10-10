#Suma y multiplicacion Ejercicio 9
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Ejercicio 9")
print (" ")
#Definir el valor de la suma
def suma(numeros):
    total = 0  # Inicializa el total en 0
    for num in numeros:  # Usa 'numeros' como el argumento de entrada
        total += num  # Suma cada número a total
    return total  # Devuelve el total

# Definir la función de multiplicación
def multiplicacion(numeros):
    r = 1  # Inicializa el resultado en 1
    for num in numeros:  # Usa 'numeros' como el argumento de entrada
        r *= num  # Multiplica cada número por r
    return r  # Devuelve el resultado

# Sumar y multiplicar la lista
thislist = [1, 2, 3, 4]
s = suma(thislist)
m = multiplicacion(thislist)

# Resultados
print("El resultado de la suma es:", s)           
print("El resultado de la multiplicación es:", m)   


