#crear diccionarios

#estructura de un diccionario
diccionario = {
    "clave_1": "valor 1",
    "clave_2": "valor 2",
    "clave_3": "valor 3"
}

diccionario_aprendiz= {
    "nombre": "Daniel",
    "apellido": "Acosta",
    "programa": "ADSO",
    "ficha": "3321349",
    "edad": 18,
}
print(type(diccionario_aprendiz))

#acceder a un valor de un diccionario
print(diccionario_aprendiz["nombre"])
print(diccionario_aprendiz.get("apellido"))

#acceder a las claves de un diccionario
print( diccionario_aprendiz.keys())

#acceder a los valores de un diccionario
print(diccionario_aprendiz.values())

#obtetener la clave y un valor de un diccionario
print(diccionario_aprendiz.items())

#agegar un nuevo valor a un diccionario
diccionario_aprendiz["correo"] = "daniel.acosta@correo.com"

#modificar un valor de un diccionario
diccionario_aprendiz["edad"] = 19
print(diccionario_aprendiz)

#metodo update 
diccionario_aprendiz.update({"programa": "Analisis y desarrollo de software"})

#comprobar si una clave existe en un diccionario

for clave in diccionario_aprendiz.keys(): #imprime las claves del diccionario
    print(clave)
print("\n")
for valor in diccionario_aprendiz.values(): #imprime los valores del diccionario
    print(valor)


#clave y valor a la vez
for clave, valor in diccionario_aprendiz.items():
    print(f"clave: {clave} - valor: {valor}")   

diccionario_aprendiz.popitem() #elimina el ultimo elemento del diccionario
print(diccionario_aprendiz)

diccionario_aprendiz.pop("edad") #elimina el elemento con la clave "edad"
print(diccionario_aprendiz)

diccionario_aprendiz.clear() #elimina todos los elementos del diccionario
print(diccionario_aprendiz)

#setdefault
diccionario_aprendiz.setdefault("nombre", "Daniel") #si la clave "nombre"

#diccionarios anidados
diccionario_anidado = {
    "aprendiz_1": {
        "nombre": "Daniel",
        "apellido": "Acosta",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 32
    },
    "aprendiz_2": {
        "nombre": "Maria",
        "apellido": "Gomez",
        "programa": "ADSO",
        "ficha": "3321349",
        "edad": 28
    },
        "aprendiz_3": {
        "nombre": "jorge",
        "apellido": "garzon",
        "programa": "topografia",
        "ficha": "3321359",
        "edad": 23
    }
}

#acceder a un valor de un diccionario anidado
print(diccionario_anidado["aprendiz_1"]["nombre"])

#recorrer un diccionario anidado
for aprendiz, datos in diccionario_anidado.items(): #dato nos sirve para acceder a los valores del diccionario anidado
    print(f"Aprendiz: {aprendiz}")
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
