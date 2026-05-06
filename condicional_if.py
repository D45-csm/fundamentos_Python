""" if  True:
    print("e veldad")
elif True:
    print("la condicion e falsa")
else:
    print("la condicion otra ve es falsa")



     
edad= int(input("ingresa tu edad"))

if edad<18:
    if edad>12 and edad<18 :
        print("eres un adolescente ")
    else :
        print("niño")    
else:
    if edad>=18 and edad<60 :
        print("eres un adulto que paga impuestos")
    else :
        print("eres un adulto mayor") 

         """

numero= int(input("ingresa un numero: "))

if numero %2 ==0 :
    print("el numero es par")
else:
    print("el numero es impar")

print("es par" if numero %2 ==0  else "impar") #operador ternario