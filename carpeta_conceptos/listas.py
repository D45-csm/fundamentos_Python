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