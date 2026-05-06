
a=5
b=10
#suma
suma=a + b
print("suma total: ",suma)

#resta
resta=a - b
print("resta total: ",resta)

#multiplicacion
multiplicacion=a * b
print("multiplicacion total: ",multiplicacion)

#divicion
divicion=a / b
print("divicion total: ",divicion)

#divicion entera
div_entera =a // b
print("divicion entera total: ",div_entera)


#modulo
modulo=a % b
print("modulo total: ",modulo)

#potencia
potencia=a ** b
print("potencia total: ",potencia)

#PRESEDENCIA DE OPERACIONES
resultado= a + b*3 #siempre se realiza de adentro hacia afuera
print(" total: ",resultado) #en este caso se resuelve primero la * luego +

resultado= (a + b) *2  
print(" total: ",resultado)

resultado= a * b //3  
print(" total: ",resultado)

resultado = ((a + b) *(a - b)/(a * b) )- ((a ** b) %3)
print(" total: ",resultado)


import math
print(math.pi)
print(math.e)
print(math.sqrt(16))

import random 

random.random() # numero aleatorio del 0 al 1
numero_aleatorio= random.randint(1,10)
print(numero_aleatorio)