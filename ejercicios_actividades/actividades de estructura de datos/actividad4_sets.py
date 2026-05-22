#Análisis de Matrículas del Centro de Formación

#punto 1
python_curso ={'Ana','Luis','Marta','Carlos','Sofia','Pedro'} 
java_curso ={'Luis','Carlos','Pedro','Laura','Diego'}
bd_curso ={'Marta','Sofia','Laura','Ana','Miguel'}

#punto 2
#unión de los tres cursos
print("punto 2")
print(f"el total de aprendices únicos en los tres programas: {len(python_curso | java_curso | bd_curso)}")

# aprendices cursando python y java simultáneamente
print(f"los aprendices que cursan Python Y Java simultáneamente {python_curso & java_curso}")  

# devs de solo python
print(f"los aprendices que solo están en Python: {python_curso - (java_curso | bd_curso)}")

# solo aprendices con dos cusrsos 
print(f"aprendices que están en exactamente dos programas: "
f" {(python_curso & java_curso) | (python_curso & bd_curso) | (java_curso & bd_curso) - (python_curso & java_curso & bd_curso)}")

#punto 3
inscripciones= ['Ana','Luis', 'Ana', 'Marta', 'Carlos', 'Luis', 'Sofia','Pedro','Ana']
print("punto 3")
print("aprendices unicos inscritos: ", set(inscripciones)) 

#punto 4

#numero de programas a los que esta inscrito cada persona
conteo_programas= {aprendiz: inscripciones.count(aprendiz) for aprendiz in set(inscripciones)}
print("punto 4")
print(conteo_programas)

#punto 5 bonus
print("punto 5 bonus")
print("hay aprendices inscritos en los tres programas") if python_curso & java_curso & bd_curso else print("no hay aprendices inscritos en los tres programas")



