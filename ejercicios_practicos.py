import math
""" ejercicio 1 """
nombre= "daniel"
valor_producto= 2000
promedio_asignatura=float(3.0)

print(nombre , valor_producto, promedio_asignatura)

""" ejercicio 2 """
var_int_1=5
var_int_2=76
var_float=float(3.55)
var_string_1= "hola"
var_string_2= "que tal"

print(f"{var_int_1} + {var_int_2} + {var_float}= {var_int_1 + var_int_2 + var_float} ")

print(max(var_int_1, var_int_2))

print(var_float/(var_int_1%var_int_2))

print(var_string_1 , var_string_2)

""" ejercicio 3 """
base= 5
exponente= 4
print(math.pow(base, exponente))

""" ejercicio 4 """

print(math.sqrt(2))
print(math.sqrt(8))
print(math.sqrt(9))
print(math.sqrt(27))
print(math.sqrt(28))
print(math.sqrt(55))
print(math.sqrt(121))

""" ejercicio 5 """
estudiante = "Daniel Acosta"
nota1=8.5
nota2= 9.0
nota3=7.5
nota4= 10.0
nota5= 6.0

promedio= (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Estudiante:", estudiante)
print("Promedio final:", promedio)

""" ejercicio 6 """
numeroUno= 8
numeroDos= 2

auxiliar= numeroUno   
numeroUno= numeroDos  
numeroDos= auxiliar   

print("Valor de numeroUno:", numeroUno)
print("Valor de numeroDos:", numeroDos)

""" ejercicio 7 """
Estado= (5 == 2) or (2 > 1)
print("El resultado de la variable Estado es:", Estado)

""" ejercicio 8 """
Resultado= (10 + 5)*2 /3 -(4 ** 2) + (8 * 2)
print("el resultado de la operación es:", Resultado)

""" ejercicio 9 """
# cuadrado
ladoCuadrado= 8
print(f"perimetro del cuadrado: {4*ladoCuadrado}  area del cuadrado: {ladoCuadrado**2}")

#triangulo
baseTriangulo= 9
alturaTriangulo= 8
ladoUnoTriangulo=8
ladoDosTriangulo=8

print(f"perimetro del Triangulo: {ladoUnoTriangulo + ladoDosTriangulo + baseTriangulo }  área del Triangulo: {(baseTriangulo*alturaTriangulo)/2}")

#rectangulo 
baseRectangulo= 8
alturaRectangulo= 6

print(f"perimetro del Rectangulo: {2*baseRectangulo + alturaRectangulo*2}  area del Rec: {baseRectangulo*alturaRectangulo}")

""" ejercicio 10 """
# Pedir la edad al usuario
edad = int(input("Ingresa la edad: "))

# Clasificación directa con impresión inmediata
if edad >= 0 and edad <= 5:
    print("Categoría: Infante")
elif edad >= 6 and edad <= 10:
    print("Categoría: Niño")
elif edad >= 11 and edad <= 15:
    print("Categoría: Pre adolescente")
elif edad >= 16 and edad <= 18:
    print("Categoría: Adolescente")
elif edad >= 19 and edad <= 25:
    print("Categoría: Pre adulto")
elif edad >= 26 and edad <= 40:
    print("Categoría: Adulto")
elif edad >= 41 and edad <= 55:
    print("Categoría: Pre anciano")
elif edad >= 56:
    print("Categoría: Anciano")
else:
    print("Error: La edad no puede ser negativa")
    

