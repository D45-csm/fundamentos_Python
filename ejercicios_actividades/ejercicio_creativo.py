#PIEDRA PAPEL O TIJERA
import random 

#funcion para que el sistema elija al azar una alternativa
def opcion_sistema():
    opciones = ["PIEDRA", "PAPEL", "TIJERA"]
    return random.choice(opciones).upper()

print("juguemos piedra, papel o tijera \n elige una opcion: \n 1)Piedra \n 2)Papel \n 3)Tijera")

# validacion de ingreso de opcion de usuario
while True:
    intento_usuario = input("ingresa una opcion (1, 2 o 3): ")
    
    # 1. Verificamos si el texto NO está compuesto por números
    if not intento_usuario.isdigit():
        print("❌ Error: No se permiten letras ni símbolos. Debes ingresar un número.\n")
        continue # Hace que el bucle vuelva a empezar desde el input
        
    # 2. Si pasa la prueba anterior, verificamos que sea un número válido (1, 2 o 3)
    if intento_usuario in ["1", "2", "3"]:
        break # Rompe el bucle porque la respuesta es correcta
    else:
        print("❌ Error: Opción inválida. Elige estrictamente un número entre 1, 2 o 3.\n")

#combertir dato a un int
intento_usuario=int(intento_usuario)
#mantener en pie la opciion del sistema
eleccion_sistema= opcion_sistema()

#posibilidades de decicion final -----

#si el usuario toma la decision 1 (piedra)
if intento_usuario==1 :
    if eleccion_sistema=="PIEDRA" :
        print(f"Tu:Piedra vs IA:{eleccion_sistema} \n resultado: ES EMPATE 🫥😶")
    elif eleccion_sistema=="PAPEL" :
        print(f"Tu:Piedra vs IA:{eleccion_sistema} \n resultado: TU PIERDES 🤣")
    elif eleccion_sistema=="TIJERA" :
        print(f"Tu:Piedra vs IA:{eleccion_sistema} \n resultado: TU GANAS 😒")
#si el usuario toma la desicion de 2 (papel)        
if intento_usuario==2 :
    if eleccion_sistema=="PIEDRA" :
        print(f"Tu:Papel vs IA:{eleccion_sistema} \n resultado: TU GANAS 😒")
    elif eleccion_sistema=="PAPEL" :
        print(f"Tu:Papel vs IA:{eleccion_sistema} \n resultado: ES EMPATE 🫥😶")
    elif eleccion_sistema=="TIJERA" :
        print(f"Tu:Papel vs IA:{eleccion_sistema} \n resultado: TU PIERDES 🤣")
#si el usuario toma la desicion de 3 (tijera)
if intento_usuario==3 :
    if eleccion_sistema=="PIEDRA" :
        print(f"Tu:Tijera vs IA:{eleccion_sistema} \n resultado: TU PIERDES 🤣")
    elif eleccion_sistema=="PAPEL" :
        print(f"Tu:Tijera vs IA:{eleccion_sistema} \n resultado: TU GANAS 😒")
    elif eleccion_sistema=="TIJERA" :
        print(f"Tu:Tijera vs IA:{eleccion_sistema} \n resultado: ES EMPATE 🫥😶")
#fin de codigo____ realizado por: Daniel Acosta González 