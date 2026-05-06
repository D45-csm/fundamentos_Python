peso= float(input("ingresa tu peso en 'kg': "))
altura= float(input("ingresa tu altura en 'm': "))

imc= peso/(altura**2)


if imc <18.5 :
    print("peso bajo:{imc}")
elif imc>=18.5 or imc<24.9 :
    print("peso normal: {imc}")
elif imc>=24.9 or imc<29.9 :
    print("sobrepeso: {imc}")
else:
    print("obesidad: {imc}")