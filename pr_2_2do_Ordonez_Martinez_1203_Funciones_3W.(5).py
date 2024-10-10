#Area y volumen Ejercicio 5
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


