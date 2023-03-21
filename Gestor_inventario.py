class Producto:
    def __init__(self, precio, cantidad, codigo, descripcion, nombre): 
        self.precio = precio
        self.cantidad = cantidad
        self.codigo = codigo
        self.descripcion = descripcion
        self.nombre = nombre
        
    def obtener_total(self):
        return self.precio * self.cantidad
    def __str__(self):
        return f"{self.nombre}: {self.cantidad} x ${self.precio} = ${self.obtener_total()}"
class ventas:
    def __init__(self):
        self.pro_ven=[]
    def agre_pro(self, producto):
        self.pro_ven.append(producto)
    def mostrar_producto(self):
        total = 0
        for producto in self.pro_ven:
            print(producto)
            total += producto.

class Pedido:
    def  __init__(self, productos, n_cliente, cantidad, direccion):
        self.productos = productos
        self.cantidad = cantidad
        self.n_cliente = n_cliente
        self.n_direccion = direccion
    
class Gestor_Inventario:
    def __init__(self, productos, cantidad):
        self.productos = productos
        self.cantidad = cantidad
    
    
    def actualizar_inventario(self, productos, cantidad ):
        for i in enumerate(None):
            pass

class Generador_Reporte: 
    def __init__(self, productos, codigo, ganancias, cantidad):
        self.productos = productos
        self.codigo = codigo
        self.ganancias = ganancias
        self.cantidad = cantidad

def menu():
    print("Menú".center(60,"*"))
    print("1. Mostrar Productos")
    print("2. Mostrar Pedido")
    print("3. Completar Pago")
    print("4. Inventario")
    print("5. Reporte")
    print("6. Salir")
    
def menu_productos():
    print("Leche")
    print("Arroz")
    print("Aceite")
    print("Atún")
    
menu()
cliente = int(input("Ingrese una opcion: "))
if cliente == 1:
    pass

elif cliente == 2:
    pass



        