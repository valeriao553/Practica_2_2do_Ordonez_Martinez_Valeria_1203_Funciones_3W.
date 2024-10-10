# Tres numeros Ejercicio 8
print(" ")
print ("Ordonez Martinez Valeria 3W 1203, Ejercicio 8")
print(" ")
#Pedir al usuario que ingrese tres valores
x=int(input("Ingrese el primer numero: "))
y=int(input("Ingrese el segundo numero: "))
z=int(input("Ingrese el tercer numero: "))
print(" ")
#Definir la funcion
def mi_funcion(x,y,z):
    #Comparar cual es mayor
    mayor= max(x, y,z)
    #Mostrar resultado
    print("El mayor es: ", mayor)
#Llamar funcion    
mi_funcion(x,y,z)
print(" ")