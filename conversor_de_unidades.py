"""Proyecto de conversor de unidades en Python"""

print("Bienvenido al conversor de unidades")

print("Seleccione la unidad que desea convertir: ")

print("\n1. Metros a pies")
print("2. Metros a pulgadas")
print("3. Metros a yardas")
print("4. Metros a millas")

unidad = input("\n Ingrese el numero de la unidad que desea convertir: ")

def conversion(unidad):
    if unidad == "1":
        metros = int(input("Ingrese los metros que desea convertir: "))
        print("El resultado de la conversion es: ", metros * 3.28084)
    elif unidad == "2":
        metros = int(input("Ingrese los metros que desea convertir: "))
        print("El resultado de la conversion es: ", metros * 39.3701)
    elif unidad == "3":
        metros = int(input("Ingrese los metros que desea convertir: "))
        print("El resultado de la conversion es: ", metros * 1.09361)
    elif unidad == "4":
        metros = int(input("Ingrese los metros que desea convertir: "))
        print("El resultado de la conversion es: ", metros * 0.000621371)
    else:
        print("Unidad no valida")

conversion(unidad)