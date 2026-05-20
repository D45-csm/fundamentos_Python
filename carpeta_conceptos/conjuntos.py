
#crear conjuntos



conjunto1 = set()
conjunto2 = {1, 2, 3, 4, 5}

print(type(conjunto1))
print(type(conjunto2))

lenguajes = {"Python", "Java", "C++", "Java"}
print(lenguajes) # no se permiten elementos duplicados

#modificar conjuntos
lenguajes.add("JavaScript") #agregar un nuevo elemento
print(lenguajes)

lenguajes.remove("C++") #eliminar un elemento
print(lenguajes)

lenguajes.discard("Ruby") #eliminar un elemento sin generar error si no existe
print(lenguajes)

elemento= lenguajes.pop() #elimina un elemento aleatorio
print(f"Elemento eliminado: {elemento}")

print("java" in lenguajes) #verificar si un elemento existe en el conjunto
print("Java" in lenguajes) #verificar si un elemento existe en el conjunto


#conjuntos
python_devs= {"luis", "carlos", "meison", "maria", "ana"}
java_devs= {"carlos", "ana", "maria", "luis", "pedro"}

#union de conjuntos
todos_los_devs = python_devs | java_devs #tambien se puede usar python_devs.union(java_devs)
#no repite elemntos comunes

print(todos_los_devs)

#interseccion de conjuntos
devs_comunes = python_devs & java_devs #tambien se puede usar python_devs.intersection(java_devs)

print(devs_comunes)

#diferencia de conjuntos
solo_python_devs = python_devs - java_devs #tambien se puede usar python_devs.difference(java_devs)
#los que estan en python_devs pero no en java_devs
print("solo python devs: ", solo_python_devs)

solo_python_devs = java_devs-python_devs 
    
print("solo java devs: ", solo_python_devs) #los que estan en java_devs pero no en python_devs

#diferencia simetrica
devs_unicos = python_devs ^ java_devs #tambien se puede usar python_devs.symmetric_difference(java_devs)
#los que estan en python_devs o en java_devs pero no en ambos
print("devs unicos: ", devs_unicos)

