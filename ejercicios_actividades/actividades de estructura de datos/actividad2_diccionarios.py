#sistema de regisrto de aprendices
#punto 1
grupo={
    "3321349": {
        "nombre": "Daniel",
        "edad": 18,
        "notas": [2.7, 1.0, 3.5],
        "ciudad": "Bogota",
            },
    "3323267": {
            "nombre": "Martha",
            "edad": 23,
            "notas": [3.5, 2.0, 5.0],
            "ciudad": "barranquilla",
            },
    "3321348": {
            "nombre": "Carlos",
            "edad": 20,
            "notas": [4.0, 4.0, 4.0],
            "ciudad": "Medellin",
           },
    "2356764": {
            "nombre": "Antonio",
            "edad": 19,
            "notas": [3.5, 4.0, 4.5],
            "ciudad": "Medellin",

            }
}


#punto 2 y 3
#funcion para calcular el promedio de las notas de cada aprendiz
def calcular_promedio(notas):
    promedio=sum(notas) /len(notas)
    return promedio



#reporte del diccionario 
for ficha, aprendiz in grupo.items():
    promedio=calcular_promedio(aprendiz['notas'])
    estdo= "aprobado" if promedio >= 3.0 else "reprobado"
    print(f"Ficha: {ficha}")
    print(f"Nombre: {aprendiz['nombre']}")
    print(f"Edad: {aprendiz['edad']}")
    print(f"Notas: {aprendiz['notas']}")
    print(f"Promedio: {promedio} | Estado: {estdo}")
    print(f"Ciudad: {aprendiz['ciudad']}")
    print("-" * 30)

#punto 4
#agregar nuevo aprendiz
grupo["3247898"] = {
    "nombre": "Ana",
    "edad": 22,
    "notas": [3.0, 3.5, 4.0],
    "ciudad": "Cali"
}
#actualizar ciudad de un aprendiz
grupo["3321349"]["ciudad"] = "ibague"

#punto 5
# x[1] representa el diccionario interno de cada aprendiz, accedemos a sus "notas" y calculamos el promedio.
aprendices_oredenados=sorted(grupo.items(), key=lambda x:calcular_promedio(x[1]['notas']), reverse=True)

for ficha, aprendiz in aprendices_oredenados:
    promedio=calcular_promedio(aprendiz['notas'])
    estdo= "aprobado" if promedio >= 3.0 else "reprobado"
    print(f"Ficha: {ficha} | Nombre: {aprendiz['nombre']} | Promedio: {promedio:.2f} | Estado: {estdo}")