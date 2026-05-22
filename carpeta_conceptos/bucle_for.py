lenguaje="Python"

for  letra in lenguaje:
    print(letra)

frutas = ["manzana", "pera", "naranja"]


#break: para salir del bucle
for fruta in frutas:

    if fruta == "manzana":
        #break
        continue #salta a la siguiente iteración
    print(fruta)
else: 
    print("El bucle ha terminado")
    #El bloque else se ejecuta cuando el bucle termina normalmente, es decir, sin un break.

#range: para generar una secuencia de números
for i in range(5):
    print(i)    
print ("---")
#range(inicio, fin, paso)
for i in range(1, 10, 2):
    print(i)
    pass #pass es una declaración vacía que se utiliza como marcador de posición cuando se requiere 
#una declaración sintácticamente pero no se desea ejecutar ningún código.

#recorrer una tupla con for
colores = ("rojo", "verde", "azul")
for color in colores:
    print(color)

#recorrer un diccionario con for
persona = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
