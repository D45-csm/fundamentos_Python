#estructura de una tupla

tupla=("elemnyo 1", "elemnto 2", "elemento 3")

print(type(tupla))

tupla_2= "e", "r", "y"
print(type(tupla_2)) #<class 'tuple'>



tupla_3= ("hola")
print(tupla_3) #si la tupla no tiene "," lo registr como otro tipo de dato

tupla_4=tuple("hola")  #si agregamos esta funcion, hace que la palabra sea un eleemnto por aparte
print(tupla_4) #= ('h', 'o', 'l','a')

tupla_mixta=("gol", 43, True)
print(tupla_mixta)

#buscar elementos en una tupla
aprendices=("jhon", "andres", "stephanie")
print(aprendices[2])


""" aprendices[0]="mario " """ #si intentamos cambiar algun valor de una tupla 
#nos va a dar un error

#concatenar tuplas
numeros_1=(1,2,3)
numeros_2=(4,5,6)
numeros_concatenados=numeros_1 + numeros_2
print(numeros_concatenados)

#multiplicar tuplas
numeros_multiplicados=numeros_1*3  
print(numeros_multiplicados)

#medir la longitud de una tupla
print(len(numeros_concatenados))

#contar elementos de una tupla
print(aprendices.count("andres")) 

#obtener el indice de un elemento
print(aprendices.index("stephanie"))

#modificar una tupla en una lista
print(type(aprendices)) #tupla original   
aprendices_lista=list(aprendices) #convertimos la tupla en una lista
print(type(aprendices_lista)) 

aprendices_lista.append("felipe")
print(aprendices_lista) #agregamos un nuevo elemento a la lista
aprendices=tuple(aprendices_lista) #convertimos la lista nuevamente en tupla
print(type(aprendices)) #tupla modificada

#verificar si un elemento existe en una tupla
print("andres" in aprendices) #true 

#empaquetar y desempaquetar tuplas
#empaquetadas
programa_1="ADSO"
programa_2="SST"
programa_3="TOPOGRAFIA"
tupla_programas=programa_1, programa_2, programa_3 #empaquetamos las variables en una tupla
print(tupla_programas)

#desempaquetar 
tupla_programas= ("ADSO", "SST", "TOPOGRAFIA")
programa_a, programa_b, programa_c=tupla_programas #desempaquetamos la tupla en variables individuales
print(programa_a)

tupla_ciudades= ("bucaramanga", "medellin", "cali", "bogota")
ciudad_a, ciudad_b, ciudad_c,ciudad_d=tupla_ciudades
print(ciudad_c)

#iterar sobre una tupla 
for programa in tupla_programas:
    print(programa)

