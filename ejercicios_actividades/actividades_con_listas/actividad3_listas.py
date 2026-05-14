#Gestión de Lista de Reproducción Musical
# punto 1

#declaramos la lista de canciones
canciones=["la cantata del diablo", "bandera negra", "mery on a cross", "fiesta pagana", "xanandra"]

#punto 2

#agregar nueva cancion
canciones.append("molinos de viento")
#agregar nueva cancion en la posicion 2
canciones.insert(2, "cadaveria")
#agregar lista nueva de canciones
canciones.extend(["Bonus Track 1", "Bonus Track 2"])

#punto 3

#remover por nombre de cancion 
canciones.remove("fiesta pagana")
#remover ultima cancion 
print(canciones.pop())

#punto 4
# organizar playlist en orden alfabetico
canciones.sort()
print(canciones)

#punto 5
#solucion de preguntas
print(f"la playlist tiene: {len(canciones)} canciones")
print(f"la posicion de la primera cancion agregada es: {canciones[canciones.index("la cantata del diablo")]}")
print(f"las veces que aparece la cancion 'Bonus Track 1' son: {canciones.count("Bonus Track 1")} vez/veces")