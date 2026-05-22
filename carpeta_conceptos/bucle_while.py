i=0

while i<6:
    print("Hola Mundo")
    i+=2

#tambien se puede utilizar el break para salir del bucle
i=0
print("---")
while True:
    print("Hola Mundo")
    i+=2
    if i==4:
        break
#tambien se puede utilizar el continue para saltar a la siguiente iteracion
i=7
print("---")
while i<6:
    i+=1
    if i==3:
        continue #saltamos el numero 3
    print("Hola Mundo", i)
else:
    print("El bucle ha terminado")



#juego de pokemon

puntos_vida=100
pokemon= input("¿Qué pokemon quieres usar? (Pikachu, Charmander, Bulbasaur): ")
while puntos_vida>0:
    print(f"Tu {pokemon} tiene {puntos_vida} puntos de vida")
    puntos_vida-= int(input("¿Cuánto daño quieres hacer? "))
print(f"Tu {pokemon} ha sido derrotado")

