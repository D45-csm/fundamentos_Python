

"""en python no se puede usar numeros o caracteres especiales
al inicio del nombre de una variable, tampoco palabras claves de
python, tampoco espacios en blanco 
"""
"""---------------------------------------------------------"""
"""una buena practica es hacer camelcase, que es poner en mayuscula 
en el primera letra de la palabra"""

CursoActual= input("ingresa el curso actual: ")

print(f"hola mundo, estamos en el curso {CursoActual}")
"""----------------------------------------------------------"""
#tipos de dato que no conozco
datoSTR= """ ESTO ERS UN DATO STR"""

datoComplex= 4 + 3j #tipo de dato complejo 

frutas = ["manzana", "banana", "cereza"] # listas
frutas.append("naranja")  # agrega nuevo elemento
print(frutas[0])          # el 0 es el dato que se extraera 0= manzana 1= banana

coordenadas = (10, 20,5) #tuplas: no se pueden cambiar una vez creadas

for i in range(1, 5):
    print(i)  # 



#tipos de escritura de variables
""" Nombre= "daniel"
Apellido= "acosta"
edad= 18
altura=1.76 
activo=False
telefono= 3118689862
cedula= 1107979169
cedula_str= str(cedula)
        
print(type(Nombre), Nombre)
print(type(Apellido), Apellido)
print(type(edad), edad )
print(type(altura), altura)
print(type(activo), activo)
print(type(telefono),telefono)

altura= float(altura)
print(" ")
print(type(Nombre), Nombre)
print(type(Apellido), Apellido)
print(type(edad), edad)
print(type(altura), altura)
print(type(activo), activo)

print(type(telefono),telefono)
print(type(cedula_str),cedula_str)  """
"""
if type(telefono)== int :
    telefono= str(telefono)
    print (type(telefono), "era entero")
""" 



""" nombre_completo= input("ingrese su nombre completo: ")
print(nombre_completo) """


# Input
nombre_completo = input("Ingrese su nombre y apellido: ")
print("que tal ", nombre_completo)

edad_aprendiz = int(input("que edad tienes: "))
print(f"eres {nombre_completo} y tienes {edad_aprendiz} años")
print(type(edad_aprendiz))