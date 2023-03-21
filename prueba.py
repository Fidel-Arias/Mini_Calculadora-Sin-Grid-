class Producto:
    def __init__(self, nombre, precio, cantidad, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion

class Pedido:
    def __init__(self, productos, cantidades):
        self.productos = productos
        self.cantidades = cantidades

class GestorDeInventario:
    def __init__(self, productos):
        self.productos = productos
    
    def actualizar_inventario(self, pedido):
        for i, producto in enumerate(pedido.productos):
            self.productos[i].cantidad -= pedido.cantidades[i]

class GeneradorDeReportes:
    def __init__(self, productos_vendidos):
        self.productos_vendidos = productos_vendidos
    
    def generar_reporte_inventario(self):
        total = sum([p.precio * p.cantidad for p in self.productos_vendidos])
        print(f"Inventario total: {total}")
    
    def generar_reporte_ventas(self):
        ventas_por_producto = {}
        for p in self.productos_vendidos:
            if p.nombre in ventas_por_producto:
                ventas_por_producto[p.nombre] += p.precio * p.cantidad
            else:
                ventas_por_producto[p.nombre] = p.precio * p.cantidad
        
        for nombre, ventas in ventas_por_producto.items():
            print(f"Producto: {nombre} - Ventas: {ventas}")
            
            
            
            
            
            
#menu de prueba

# Crear un diccionario de productos con sus precios
productos = {"Manzanas": 2.5, "Plátanos": 1.8, "Naranjas": 3.0, "Pera": 2.0}

# Crear una función para mostrar el menú de opciones
def mostrar_menu():
    print("==== MENÚ DE COMPRAS ====")
    for producto, precio in productos.items():
        print(f"{producto} - ${precio}")
    print("========================")

# Crear una función para solicitar al usuario la selección de un producto
def seleccionar_producto():
    producto = input("Ingrese el nombre del producto: ")
    while producto not in productos:
        producto = input("Producto no encontrado. Ingrese otro nombre: ")
    return producto

# Crear una función para solicitar al usuario la cantidad de un producto
def seleccionar_cantidad():
    cantidad = int(input("Ingrese la cantidad de productos que desea comprar: "))
    while cantidad <= 0:
        cantidad = int(input("Cantidad inválida. Ingrese otro número: "))
    return cantidad

# Crear una función para calcular el total de la compra
def calcular_total(producto, cantidad):
    return productos[producto] * cantidad

# Mostrar el menú y solicitar la selección del usuario
mostrar_menu()
producto_seleccionado = seleccionar_producto()

# Solicitar la cantidad de productos
cantidad_seleccionada = seleccionar_cantidad()

# Calcular el total y mostrar el resultado al usuario
total_compra = calcular_total(producto_seleccionado, cantidad_seleccionada)
print(f"El total de la compra es: ${total_compra}")

