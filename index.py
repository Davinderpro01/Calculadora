print(" ")
print("                                       2 Hola y bienvenido a la calculadora virtual de Devin")
print("    1. suma")
print("    2. resta")
print("    3. multiplicación")
print("    4. división")
print("    5. residuo")
print(" ")
operacion = int(input("introduce el número de la operación que deseas  =  "))

if operacion == 1:
    print(" ")
    print("Usted eligió la operación de suma, esta será con 2 números")
    numero1 = int(input("ingrese el primer número = "))
    numero2 = int(input("ingrese el segundo número = "))
    suma = numero1+numero2
    print("su resultado es") 
    print(suma)

if operacion == 2:
    print(" ")
    print("Usted eligió la operación de resta, esta será con 2 números")
    numero1 = int(input("ingrese el primer número = "))
    numero2 = int(input("ingrese el segundo número = "))
    resta = numero1-numero2
    print("su resultado es") 
    print(resta)

if operacion == 3:
    print(" ")
    print("Usted eligió la operación de multiplicación, esta será con 2 números")
    numero1 = int(input("ingrese el primer número = "))
    numero2 = int(input("ingrese el segundo número = "))
    multiplicacion = numero1*numero2
    print("su resultado es") 
    print(multiplicacion)

if operacion == 4:
    print(" ")
    print("Usted eligió la operación de división, esta será con 2 números")
    numero1 = int(input("ingrese el primer número = "))
    numero2 = int(input("ingrese el segundo número = "))
    division = numero1/numero2
    print("su resultado es") 
    print(division)

if operacion == 5:
    print(" ")
    print("Usted eligió la operación de residuo, esta será con 2 números")
    numero1 = int(input("ingrese el primer número = "))
    numero2 = int(input("ingrese el segundo número = "))
    residuo = numero1%numero2
    print("su resultado es") 
    print(residuo)

if operacion > 5:
    print("escoja una de las opciones del 1 al 5")
    
if operacion == 0:
    print("escoja una de las opciones del 1 al 5")