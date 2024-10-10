#Email Ejercicio 6
print (" ")
print ("Ordonez Martinez Valeria 3W 1203, Ejercicio 6")
print (" ")
#Definir funcion
def Email():
    #Solicitar al usuario que ingrese su correo electronico
    email = input("Ingrese su correo electrónico: ")
    print(" ")
    #Agregar condicion para ssaber si es valida o no
    if "@" in email:
        print("Si es válida.")
    else:
        print("No es válida.")
# Llamar a la función
Email()
print(" ")




