#Análisis de Temperaturas Semanales
#punto 1
temperaturas = [18, 21, 19, 24, 22, 20, 17, 23, 25, 21, 18,20, 22, 19]

#punto 2
print("primer dia: ", temperaturas[0])
print("ultimo dia: ", temperaturas[-1])
print("dia 7: ", temperaturas[len(temperaturas)//2])
print("primer dia: ", temperaturas[-2])

#punto 3
print("primera semana: ",temperaturas[:7])
print("segunda semana: ",temperaturas[7:14])
print(f"dias pares: {temperaturas[1::2]}")
print("al reves: ", temperaturas[::-1])

#punto 4
prom_sem1=round(sum(temperaturas[0:7])/len(temperaturas[0:7]),2)
prom_sem2= round(sum(temperaturas[7:14])/len(temperaturas[7:14]),2)

print(f"promedio semana 1: {prom_sem1} \n " 
f"promedio semana 2: {prom_sem2} ")

#punto 5 (bonus)
if max(prom_sem1,prom_sem2)==prom_sem1:
    print("semana con mayor temperatura promedio: semana 1: ", prom_sem1)
else:
    print("semana con mayor temperatura promedio: semana 2: ", prom_sem2)
