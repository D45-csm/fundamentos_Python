""" #and
print(True and True)
print(True and False)
print(False and False)

#or
print(True or True)
print(True or False)
print(False or False)

#not
print(not True)
print( not False) """
""" 
# Ejercicio AND

print(5 > 3 and 2 < 4) # true and true = true
print(5 > 3 and 2 > 4) # true and false = false
print(5 < 3 and 2 < 4) # false and true = false
print(5 < 3 and 2 > 4) # false and false = false

# Ejercicio OR

print(5 > 3 or 2 < 4) # true or true = true
print(5 > 3 or 2 > 4) # true or false = true
print(5 < 3 or 2 < 4) # false or true = true
print(5 < 3 or 2 > 4) # false or false = false

# Ejercicio NOT

print(not 5 > 3) # not true = false
print(not 5 < 3) # not false = true """


nota = float(input("Ingresa tu nota: "))

if nota >= 4.5:
    print("Excelente – Desempeño Superior")
elif nota >= 4.0:
    print("Muy Bien – Desempeño Alto")
elif nota >= 3.0:
    print("Bien – Desempeño Básico")
else:
    print("No aprobado – Desempeño Bajo")