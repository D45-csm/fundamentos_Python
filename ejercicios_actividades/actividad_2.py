try: 
#ingreso de datos
    num1= float(input("ingresa la nota 1: "))
    num2= float(input("ingresa la nota 2: "))
    num3= float(input("ingresa la nota 3: "))

        
#validar si las notas son de rango 1.0 a 5.0
    while num1> 5.0 or num2> 5.0 or num3 > 5.0 :
            print("solo se admiten notas menores o iguales a 5.0")
            if num1>5.0:
                num1= float(input("ingresa de nuevo la nota 1: "))
            if num2>5.0:
                num2= float(input("ingresa de nuevo la nota 2: "))
            if num3>5.0:
                num3= float(input("ingresa de nuevo la nota 3: "))
            
 #promedio
    promedio= round( (num1 + num2 + num3)/3, 2)
    #clasificacion de promedio
    if promedio>=3.0 :
            print(f"nota final: {promedio} (aprovado) \n para llegar a nota maxima necesitas: {round(5.0 -promedio,2)}")
    else:
            print(f"nota final: {promedio} (no aprovado) \n para llegar a nota maxima necesitas: {round(5.0 -promedio,2)}")

except ValueError:
    # Se ejecuta cuando float() no puede convertir la entrada
    # (por ejemplo: letras, símbolos, espacios mixtos, etc.)
    print("⚠️  Advertencia: el valor  no es válido. Solo se admiten números decimales o enteros.")
    