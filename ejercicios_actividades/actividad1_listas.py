#Inventario de la Tienda Escolar
productos=["lapicero", "borrador", "sacapuntas", "calculadora", "cuaderno", "papel"]
precios_productos=[2500.00,350.2, 400, 20900.50,8407.8,200 ]
cantidad_productos=[50, 60, 62, 3, 47, 500]

total_productos=len(productos)

print("inventario de la tienda escolar:" \
"\n productos: ", productos,
"\n precios: " , precios_productos,
"\n cantidades: ", cantidad_productos,
"\n total de prodcutos: ", total_productos ) 

for x in range(0, total_productos) :
    print(f"Producto: {productos[x]} Precio: {precios_productos[x]} Cantidad: {cantidad_productos[x]}")