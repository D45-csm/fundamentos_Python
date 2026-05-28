#open(nombre, modo) -> funcion de python para abrir archivos

#R(read) lectura
#w (write) escribir
#x (crear archivo nuevo)
# a agregar texto
from math import e


try:
    file = open("archivos.txt", "r")
    print(file.readline())
    file.close()
except FileNotFoundError:
    print("no se encontro el archivo")

#uso with para cerrar el archivo manualmente
try:
    with open("archivo.txt", "r") as file:
        print(file.readlines())
except FileNotFoundError:
    print("no se encontro el archivo")

#sobrescribir un archivo del sistema


try:
    with open("archivo.txt", "w") as file:
        file.write("muchachooooos") #sobrescribe
    with open("archivo.txt", "r") as file:   
        print(file.readline()) 
except FileNotFoundError:
    print("no se encontro el archivo")

#escribir texto nuevo
try:
    with open("archivo.txt", "a") as file:
        file.write(" \nesta noche me emborracho") #sobrescribe
    with open("archivo.txt", "r") as file:   
        print(file.readlines()) 
except FileNotFoundError:
    print("no se encontro el archivo")

#crear un archivo en python
try:
    with open("archivo_2.txt", "r") as file:
        print(file.readline())
except FileNotFoundError:
    open("archivo_2.txt", "x")
    print("archivo creado")

#crear un archivo html y agregarle texto
def crear_html(script):
    try:
        with open("virus.html", "r") as file:
            print(file.readline())
    except FileNotFoundError:
        open("virus.html", "x")
        print("archivo creado")
    
    try:
        with open("virus.html", "a") as file:
            file.write(script) #sobrescribe
        with open("virus.html", "r") as file:   
            print(file.readlines()) 
    except FileNotFoundError:
        print("no se encontro el archivo")

crear_html("<HTML><H1>HOLAAA SOY VIRUS</H1></HTML>")

