# Practica_2_2do_Ordonez_Martinez_Valeria_1203_Funciones_3W.
Practica 2

# Ejercicio 1
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Practica 2 Funciones")
print(" ")
def my_function():  #Declarar la funcion
print("Hey amigos")  #Imprimir mensaje
while True: #Crear bucle while
my_function()  # Llama a la función
#Repetir el mensaje cada vez que se pusle el numero 1
repetir = input("Si quiere volver a repetir la función pulse '1' (o cualquier otra tecla para salir): ")
print(" ")
if repetir != '1':  #Condicion de evaloacion
break  # Salir del bucle si no se presiona '1'
![image](https://github.com/user-attachments/assets/0b4c0708-0de0-4625-9267-f0d9e4c0bfb6)
![image](https://github.com/user-attachments/assets/f07b2e34-0d71-4c10-94ed-41a9b97b2cf1)


 # Ejercicio 2
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Practica 2, ejercicio 2")
print(" ")

#Solicitar al usiario igresar su nombre
nombre = str(input("Ingrese su nombre: "))
print(" ")

#Definir mi funcion
def my_function(nombre):
#Desplegar mensaje    
    print("¡Hola " + nombre + "!")

#Llamar a la función
my_function(nombre)
print(" ")
![image](https://github.com/user-attachments/assets/c2626cfe-9a75-4311-9984-d99c9dc497c5)
![image](https://github.com/user-attachments/assets/c9064622-4b23-41df-ab6b-f281dc6703f9)

# Factorial ejercicio 3
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Ejercicio 2 Factorial")
print(" ")
 #Solicitar al usuario que ingrese un número natural
print("Ingrese un número natural: ")
num = int(input())  # Convertir la entrada a un entero

#Indicar la variable fact
fact = 1

#Crear un bucle para calcular el factorial de 1 hasta num
for i in range(1, num + 1):
    # Multiplicar fact por i para ir acumulando los números
    fact *= i

#Imprimir el resultado final del factorial
print("El factorial de", num, "es:", fact)
print (" ")

![image](https://github.com/user-attachments/assets/afa9e1ba-5eaf-417c-940e-634d804ea4df)
![image](https://github.com/user-attachments/assets/b5a11f51-8253-4b02-bc7f-fa494a2db2c0)


# IVA Ejercicio 4
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Ejercicio 4")
print(" ")
#Definir funcion
def factura_total(sin_iva, iva=21):
    # Calcular el IVA
    i = sin_iva * (iva / 100)
    # Calcular el total de la factura
    total = sin_iva + i
    return total
#Pedir al usuario la cantidad sin iva
x = float(input("Cantidad sin IVA: "))
#pedir el porcentaje de iva
z = input("Ingrese el porcentaje de IVA (Si no se le aplica tendra valor de 21%): ")
#Convertirlo a float cuando se agregue el porcentaje
if z:
    z = float(z)
else:
    z = 21  # Valor si no se ingresa nada
factura_total_ = factura_total(x, z) 
#Mostrar el total:
print("El total es:", factura_total_)
print(" ")

![image](https://github.com/user-attachments/assets/8627cf47-a5ef-4ebe-9310-ae96ad1e2c10)
![image](https://github.com/user-attachments/assets/9490c2d0-ebc7-43e9-81a8-996db3ff52e3)


# Area y volumen Ejercicio 5
print(" ")
print("Ordoñez Martínez Valeria 3W 1203, Ejercicio 5")
print(" ")
#Crear la funcion del area del circulo
def area_circulo(radio):                                     
    pi = 3.1416
    area = pi * (radio ** 2)
    return area
#Crear la funcion del volumen del circulo
def volumen_circulo(radio):
    pi = 3.1416
    volumen = (4/3) * pi * (radio ** 3)
    return volumen
#Crear la funcion de la altura del cilindro
def altura_cilindro(alt):
    pi = 3.1416
    vol = pi * (radio **3) * alt
    return vol
#Solicitar al usuario que ingrese el radio y la altura del cilindro
radio = float(input("Ingrese el radio del círculo: "))
alt = float(input("Ingrese la altuta del cilindro: "))
print(" ")
#Llamar las funciones
area = area_circulo(radio)
volumen = volumen_circulo(radio)
vol = altura_cilindro(alt)
#Mostrar los resultados
print("El área del círculo es: ", area)
print("El volumen del circulo es: ", volumen)
print("El volumen del cilindro es: ", vol)
print(" ")

![image](https://github.com/user-attachments/assets/6028e795-345f-41c8-a95a-e19ab8846108)
![image](https://github.com/user-attachments/assets/1180db01-d0ed-4092-984a-b5162835201d)

# Email Ejercicio 6
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
#Llamar a la función
Email()
print(" ")

![image](https://github.com/user-attachments/assets/e7aeaed8-e3bf-46d4-b50f-64c8667174fc)
![image](https://github.com/user-attachments/assets/e5d83d74-58a5-4fbb-b4d2-a88526180e9e)

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

![image](https://github.com/user-attachments/assets/ba3ebb19-8055-4aef-8687-ece95c2ddc39)
![image](https://github.com/user-attachments/assets/4dc0748e-8f29-4f26-a74f-6e2f1a6a42b1)


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
![image](https://github.com/user-attachments/assets/bc67d43b-25fe-4f56-b8b3-8424aae97191)
![image](https://github.com/user-attachments/assets/f0b8cfdb-7649-4a05-ab8a-0c13bda28c0b)



# Suma y multiplicacion Ejercicio 9
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Ejercicio 9")
print (" ")
#Definir el valor de la suma
def suma(numeros):
    total = 0  # Inicializa el total en 0
    for num in numeros:  # Usa 'numeros' como el argumento de entrada
        total += num  # Suma cada número a total
    return total  # Devuelve el total

#Definir la función de multiplicación
def multiplicacion(numeros):
    r = 1  # Inicializa el resultado en 1
    for num in numeros:  # Usa 'numeros' como el argumento de entrada
        r *= num  # Multiplica cada número por r
    return r  # Devuelve el resultado

#Sumar y multiplicar la lista
thislist = [1, 2, 3, 4]
s = suma(thislist)
m = multiplicacion(thislist)

#Resultados
print("El resultado de la suma es:", s)           
print("El resultado de la multiplicación es:", m)   
![image](https://github.com/user-attachments/assets/2aba23a4-1bac-4cef-8fa5-140cbb59eefb)
![image](https://github.com/user-attachments/assets/003dc37d-4968-4432-ac14-5ecc8400405d)

# Vocales Ejercicio 10
print(" ")
print("Ordonez Martinez Valeria 3W 1203, Ejercicio 10")
print (" ")
#Definir funcion de las vocales
def vocal(letra):
    v = "aeiou"
    # Verificar si la letra es una vocal
    return letra in v

#Pedir al usuario ingresar una letra
a = input("Ingrese una letra: ")

#Llamar a la función con la letra que se puso
r = vocal(a)
#Crear condicion para saber si es una voval o no
if r:
    print(a, "es una vocal.")
else:
    print(a, "no es una vocal.")
    print(" ")

![image](https://github.com/user-attachments/assets/5ed5492c-fa56-4744-b1f9-35aa900e47eb)
![image](https://github.com/user-attachments/assets/67cf31ae-7114-4645-97bd-61574d6d114f)

# Distancia Ejercicio 11
print(" ")
print ("Ordonez Martinez Valeria 3W 1203, Ejercicio 11")
print (" ")

def distancia(punto1, punto2):
    return ((punto2[0] - punto1[0]) ** 2 + (punto2[1] - punto1[1]) ** 2) ** 0.5

#Ejemplo de uso
resultado = distancia((3, 4), (7, 1))
print("La distancia entre los puntos es:", resultado)
print (" ")
![image](https://github.com/user-attachments/assets/550019f7-5679-4728-9340-f5a446f1e7fb)
![image](https://github.com/user-attachments/assets/1542da34-6879-4444-9a83-122f5838bfac)



























     
     

