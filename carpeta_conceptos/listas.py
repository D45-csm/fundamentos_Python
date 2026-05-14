#listas
listas= ["objeto1","objeto2", "objeto3 "] #siempre inicia desde 0

print(type(listas))

aprendices= ["daniel","estevan", "ronald", "alejandro", "uribe", "camilo"]

#acceder aun elemento de la lista
print(aprendices[1])

#modificar elementos de listas
aprendices[2]="rodolfo"
print(aprendices[2])

#listas mixtas
lista_mixta=["daniel", 12, ["honda", "mercedes", "bentle"]]

#   recorrer una lista dentro de una lista
print(lista_mixta[2][1])

#rangos
print(aprendices[5:6])
print(aprendices[5:5])
print(aprendices[-2:-1])
print(aprendices[1::3]) #este imprime el 1 y el 2

#concatenar listas
adso_1= ["jorge","jhon","jason","daniel"]
adso_2=["walter","joan","maria","marttha"]

adso= adso_1 + adso_2
print(adso)


#index
personas=["lorenso","roman","dan", "jorge"]
index=personas.index("lorenso")
print("este", index)

#extend
adso_3321349=["daniel", "daniela", "carlos", "ronald"]
adso_2256891=["lorena", "benito", "ramon", "camilo"]

adso_3321349.extend(adso_2256891) #concatena una elementos a una lista 
print(adso_3321349)
letras=["a", "s", "r"]
letras.extend(["e","g"])
print(letras)


#len
longitud_adso=len(adso_3321349)
print(longitud_adso)


#copy
numeros=[1,4,3,5]
numeros2= numeros.copy() #copia una lista 
print(numeros)
print(numeros2)


#count
lista=[2,4,"hola", "lola", 33, 2, 4,2]
print(lista.count("hola")) #cuenta la cantidad de elementos, letras, cadenas, o numeros que se repiten 
#depentiendo cual se pida


#append
escala_mayor=["do","re","mi","fa"]
escala_mayor.append(["sol","la","si"]) #a diferencia de extend, agrega lo que se quiere como si fuera un elemento
print(escala_mayor)


#insert y remove
carros=["toyota","chebrolet", "BMW"]
carros.insert(2, "ferrari")
#insert tiene dos partes:
#el indice, que es la ´posocion donde se quiere poner
#y el elemento
print(carros)

carros.remove("toyota") #elimina el elemento ingresado
print(carros) 


#pop
frutas=["manzana", "pera", "papaya", "fresa"]

elemto_eliminado= frutas.pop() #elimina un elemento 
#si se deja vacio, elimina el ultimo elemento
#si se pone un numero (indice) eleminia ese elemento que esta en ese puesto

print(elemto_eliminado)

if "manzana" in frutas:
    print("manzana esta en la lista")
else:
    print("manzana no esta en la lista")