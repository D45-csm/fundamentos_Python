

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


