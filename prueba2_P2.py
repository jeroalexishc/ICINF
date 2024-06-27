tipo_cambio = 950  

precios_usd = []

for i in range(10):
    precio = float(input("Ingrese el precio en dólares del producto " + str(i+1) + ": "))
    precios_usd.append(precio)

precios_clp = []
for precio in precios_usd:
    precio_clp = precio * tipo_cambio
    precios_clp.append(precio_clp)

print("\nLista de precios en pesos chilenos:")
for i in range(len(precios_clp)):
    print("Producto", i+1, ":", precios_clp[i], "CLP")


