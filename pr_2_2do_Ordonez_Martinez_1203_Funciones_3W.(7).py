# Longitud Ejerciio 7
print(" ")
print ("Ordonez Martinez Valeria 3W 1203, Ejercicio 7")
print (" ")
#Definir funcion
def palabra(t):
    # Eliminar espacios 
    t = t.strip()
    # Dividir el texto en palabras
    palabras = t.split()
    # Verificar si hay palabras en el texto
    if palabras:
        # Obtener la última palabra
        u_palabra = palabras[-1]
        # Devolver la longitud de la última palabra
        return len(u_palabra)
    else:
        return 0  # Si no hay palabras, devolver 0
#Solicitar al usuario ingresar un texto
texto = input("Ingrese un texto: ")
print (" ")
longitud = palabra(texto)
print("La longitud de la última palabra es:", longitud)
print (" ")
