#IVA Ejercicio 4
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
# Pedir al usuario la cantidad sin iva
x = float(input("Cantidad sin IVA: "))
# pedir el porcentaje de iva
z = input("Ingrese el porcentaje de IVA (Si no se le aplica tendra valor de 21%): ")
#  Convertirlo a float cuando se agregue el porcentaje
if z:
    z = float(z)
else:
    z = 21  # Valor si no se ingresa nada
factura_total_ = factura_total(x, z) 
#Mostrar el total:
print("El total es:", factura_total_)
print(" ")


