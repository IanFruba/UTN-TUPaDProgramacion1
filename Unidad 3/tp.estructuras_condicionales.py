#TRABAJO PRACTICO N.3 - Estructuras CONDICIONALES

#############  EJERCICIO 1  #############

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")


#############  EJERCICIO 2  #############

nota = float(input("Ingrese su calificacion: "))
if nota >= 6:
    print ("Aprobado")
else:
    print ("Desaprobado")


#############  EJERCICIO 3  #############

num = int(input("Ingrese un numero par: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")


#############  EJERCICIO 4  #############

edad = int(input("Ingrese su edad: "))
if edad <= 12:
    print ("Eres un niño/a")
elif edad >= 12 and edad < 18:
        print ("Eres adolescente")
elif edad >= 18 and edad < 30: 
        print ("Eres adulto/a joven")
else: 
    print ("Eres adulto/a")


#############  EJERCICIO 5  #############

contra = input("Ingrese una contraseña de 8 a 14 caracteres: ")
if 8 <= len(contra) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Porfavor, ingrese una contraseña entre 8 y 14 caracteres")


#############  EJERCICIO 6  #############

from pydoc import text
import random
from statistics import mean, median, mode
num_aleatorio = [random.randint(1, 100)for i in range(50)]
print (num_aleatorio)

moda     = mode(num_aleatorio)
mediana  = median(num_aleatorio)
media    = mean(num_aleatorio)

print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana > moda:
    print ("Hay sego positivo")
elif moda > mediana > media:
    print ("Hay sego negativo")
else:
    print("No hay sego")


#############  EJERCICIO 7  #############

palabra = input("Ingrese una palabra: ")
if palabra[-1].lower() in 'aeiou':
        palabra += "!"
print (palabra)


#############  EJERCICIO 8  #############

nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
num = int(input("Elija una opcion: "))

if num == 1:
    print (nombre.upper())
elif num == 2:
    print (nombre.lower())
else:
    print (nombre.title())


#############  EJERCICIO 9  #############

magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible).")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos).")
else:  # magnitud >= 7
    print("Extremo (puede causar graves daños a gran escala).")


    #############  EJERCICIO 10  #############

    hemisferio = input("Ingresa el hemisferio en el que te encuentras (N/S): ").strip().upper()
mes = int(input("Ingresa el número del mes (1-12): "))
dia = int(input("Ingresa el día del mes: "))

if hemisferio not in ['N', 'S']:
    print("Hemisferio inválido. Usa 'N' para norte o 'S' para sur.")
else:
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"
    else:
        print("Fecha inválida.")
        exit()

    if hemisferio == 'N':
        print(f"Estás en el hemisferio norte. Es {estacion_norte}.")
    else:
        print(f"Estás en el hemisferio sur. Es {estacion_sur}.")

        
        
        
        #Ian Ruba DNI: 45768494