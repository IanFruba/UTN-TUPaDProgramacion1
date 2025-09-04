#TRABAJO PRACTICO SECUENCIALES

#   ACTIVIDAD 1
print ("Hola Mundo!")


#   ACTIVIDAD 2
nombre = input ("Ingrese su Nombre: ")
print (f"Hola {nombre}!")


#   ACTIVIDAD 3
print ("Ingrese los siguientes datos: ")
nombre = input ("Nombre: ")
apellido = input ("Apellido: ")
edad = int(input ("Edad: "))
residencia = input ("Residencia: ")

print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")


#   ACTIVIDAD 4
radio = float(input ("Ingrese el radio de un circulo: "))

area = 3.14159 * radio**2
perimetro = 2 * 3.14159 * radio


print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")


#   ACTIVIDAD 5
seg = int(input("Ingrese los segundos a transformar: "))

hs = seg/60

print (f"Transformados serian: {hs:.2f} horas")


#   ACTIVIDAD 6
num = int(input("Ingrese un numero: "))
print (f"La tabla de multiplicar del {num} es:")
print (f"{num} x 1 =", num * 1)
print (f"{num} x 2 =", num * 2)
print (f"{num} x 3 =", num * 3)
print (f"{num} x 4 =", num * 4)
print (f"{num} x 5 =", num * 5)
print (f"{num} x 6 =", num * 6)
print (f"{num} x 7 =", num * 7)
print (f"{num} x 8 =", num * 8)
print (f"{num} x 9 =", num * 9)
print (f"{num} x 10 =", num * 10)


#   ACTIVIDAD 7
num1 = int(input("Ingrese primer numero: "))
num2 = int(input("Ingrese segundo numero: "))

print ("Division: ", num1 / num2)
print ("Multiplicacion: ", num1 * num2)
print ("Suma: ", num1 + num2)
print ("Resta: ", num1 - num2)


#   ACTIVIDAD 8
altura = float(input("Ingrese su estatura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

imc = peso / altura**2

print (f"Su indice de masa corporal es de {imc:.2f}")


#   ACTIVIDAD 9
celc = int(input("Ingrese su temperatura en Celcius: ")) 

faren = (celc * 1.8) + 32

print (f"El equivalente en grados Farenheit es: {faren}°F")


#   ACTIVIDAD 10
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
num3 = float(input("Ingrese el tercer numero: "))

promedio = (num1 + num2 + num3)/ 3

print (f"El promedio es de {promedio}")
