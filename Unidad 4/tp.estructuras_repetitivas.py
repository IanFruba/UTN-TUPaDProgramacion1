# Práctico 4: Estructuras repetitivas

########## EJERCICIO 1 ########## 

import random


for i in range (-1, 100):
    print (i + 1)

########## EJERCICIO 2 ########## 

num = int(input("Ingrese un numero: "))

num = abs(num)

if num == 0:
    digitos = 1
    print("El numero ingresado tiene un digito")
else:
    digitos = 0
    while num > 0:
        num = num // 10  
        digitos += 1  
print(f"El número tiene {digitos} dígitos")

########## EJERCICIO 3 ########## 

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))

if num1 > num2:
    num1, num2 = num2, num1 

suma = 0

i = num1 + 1
while i < num2:
    suma += i
    i += 1

print (f"La suma de los numeros entre {num1} y {num2} es {suma}")

########## EJERCICIO 4 ########## 

print("Ingresa numeros para sumarlos. Ingresa 0 para finalizar")

suma = 0

while True:
    numero = int(input("Ingrese un numero: "))

    suma += numero 

    if numero == 0:
        break

print ("La suma total de los numeros ingresados es: ", suma)

######### EJERCICIO 5 ########## 

import random

print ("Adivina el numero del 1 al 9")

numero_aleatorio = random.randint(1, 9)
intentos = 0
num = 0

while num != numero_aleatorio:
    num = int(input("Ingresa un numero: "))
    intentos += 1
    if num != numero_aleatorio:
        print ("Numero equivocado, intente denuevo")
    if num == numero_aleatorio:
        print (f"Acertaste en {intentos} intentos!")

######### EJERCICIO 6 ########## 

for i in range(100, 2, -2):
    print (i)

######### EJERCICIO 7 ########## 

num = int(input("Ingrese un numero: "))
suma = 0
for num in range(num + 1):
    suma += num 
print(f"La suma de los numeros de 0 a {num} es de: ", suma)

######### EJERCICIO 8 ########## 

print ("Ingresa 100 numeros enteros: ")

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    num = int(input("Ingrese un numero: "))
    if num % 2 == 0:
        pares += 1
else:
    impares =+ 1
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print (f"Numeros pares: {pares}")
print (f"Numeros impares: {impares}")
print (f"Numeros negativos: {negativos}")
print (f"Numeros positivos: {positivos}")

######### EJERCICIO 9 ##########  

print ("Ingrese 100 numeros para calcular su media")

suma = 0

for i in range(100):
    num = int(input(f"Ingrese un numero {i + 1}: "))
    suma += num

media = suma / 100

print ("La media de los numeros ingresados es: ", media)

######### EJERCICIO 10 ##########

numero = int(input("Ingrese un numero a invertir: "))

numero_string = str(numero)
numero_invertido = numero_string[::-1]

print ("El numero invertido es: ", numero_invertido)
