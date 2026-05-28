#try prueb el codigo
#except ejecuta otro codigo dependiendo la condicion de error
#finally ejecurta codigo al final si o si

try:
    print("intentamos algo")
except:
    print("capturar error")
finally:
    print("se ejecuta si o si, y la queso")

#error valor incorrecto
try:
    edad_usuario=int(input("cuantas vueltas le has dado al sol: "))
except ValueError:#por recomendacion se debe agregar un error en especifico
    print("solo ingrese datos numericos")
    edad_usuario=input("cuantas vueltas le has dado al sol: ")

#division por cero
try:
    print(10/0)
except ZeroDivisionError:
    print("loco, tremenda huevada, eso no se puede")


