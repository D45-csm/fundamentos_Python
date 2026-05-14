#Inventario de la Tienda Escolar

#punto 1
productos=["lapicero", "borrador", "sacapuntas", "calculadora", "cuaderno", "papel"]
#punto 2
precios_productos=[2500.00,350.2, 400, 20900.50,8407.8,200 ]
#punto 3
cantidad_productos=[50, 60, 62, 3, 47, 500]

total_productos=len(productos)
#punto 4
print("inventario de la tienda escolar:" \
"\n productos: ", productos,
"\n precios: " , precios_productos,
"\n cantidades: ", cantidad_productos,
"\n total de prodcutos: ", total_productos ) 

for x in range(0, total_productos) :
    print(f"Producto: {productos[x]} Precio: {precios_productos[x]} Cantidad: {cantidad_productos[x]}")

#punto 5
print(f"tipo de dato de la lista:{type(productos)}  tipo de dato del primer elemento: {type(productos[0])}")

""" el tipo de dato de la lista nos da "list" y el primer elemento nos da "str"
la diferencia es que si tine tipo lista, almacena cualquier tipo de dato, inclusive listas; el elemento inicial es 
solo un string, lo cual lo hace solo un elemento de esta lista """