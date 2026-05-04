valor1= float(input("ingrese primer valor "))

valor2= float(input("ingrese segundo valor "))

print("elije la operacion")
print("1.suma \ 2.resta \ 3.multiplicacion \ 4.divicion \ 5.modulo \ 6.divicion_entero \ 7.potencia")
opcion= int(input("escoge una opcion (numero): "))

suma= float (valor1 +valor2)
resta= float(valor1-valor2)
multiplicacion= float(valor1*valor2)
divicion= float(valor1/valor2)
modulo= float(valor1%valor2)
divicion_entero= float(valor1//valor2)
potencia= float(valor1**valor2)

if  opcion==1 :
    print(suma)
elif opcion==2 :
    print(resta)
elif opcion==3:
    print(multiplicacion)
elif opcion==4 :
    print(divicion)
elif opcion==5 :
    print(modulo)
elif opcion==6:
    print(divicion_entero)
elif opcion==7:
    print(potencia)
elif type(opcion) != int:
    print("opcion no valida")