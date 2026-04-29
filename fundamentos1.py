
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