"""Practica del curso PYTHON"""
"""calculadora simple para sumar, restar, multiplicar y dividir"""

print("Bienvenido a la calculadora simple")

print("Seleccione la operacion que desea realizar: ")

print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

operacion = input("\n Ingrese el numero de la operacion que desea realizar: ")

def math(operacion):
    if operacion == "1":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("El resultado de la suma es: ", num1 + num2)
    elif operacion == "2":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("El resultado de la resta es: ", num1 - num2)
    elif operacion == "3":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("El resultado de la multiplicacion es: ", num1 * num2)
    elif operacion == "4":
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        print("El resultado de la division es: ", num1 / num2)
    else:
        print("Operacion no valida")

math(operacion)