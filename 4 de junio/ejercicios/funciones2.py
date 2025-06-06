def calcular_monto(precio = 0, cantidad  = 0):
    return precio * cantidad

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))

resultado = calcular_monto(precio, cantidad)
print(f"El monto total a pagar es: {resultado}")