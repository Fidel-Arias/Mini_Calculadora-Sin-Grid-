class Producto:
    def __init__(self):
        self._descripcion = input("Ingrese el nombre del producto: ")
        self._precio = int(input("Precio del producto: "))
        self._cantidad = int(input("Cantidad del producto: "))
        self.ganancias = 0


class Gestor_Inventario(Producto):
    def Almacen(self, almacen_productos):
        self.almacen_productos = almacen_productos  # Diccionario del almacén
        self.dict_productos = {
            "Nombre:": self._descripcion,
            "Precio:": self._precio,
            "Cantidad:": self._cantidad,
        }
        self.almacen_productos.append(self.dict_productos)
        return self.almacen_productos

    def Mostrar_Almacen(self):
        for products in self.almacen_productos:
            for x_name in ["Nombre:", "Precio:", "Cantidad:"]:
                print(x_name, products[x_name])

class Pedido(Gestor_Inventario):
    def __init__(self):
        super().__init__()

    def Pedido_Cliente(self, Prod_disp):
        self._Prod_disp = Prod_disp

class Generador_Reporte(Pedido):
    def __init__(self):
        self._productos_total = 0
        self._ganancias = 0
        super().__init__()
    def reporte(self):
        self._productos_total = self._productos_total + self._cantidad_total
        self._ganancias = self._ganancias + self._precio_total
    def Muestra_reporte(self):
        print(f"Total de productos comprados: {self._productos_total}")
        print("Ganancias totales: S/.", self._ganancias, ".")

def menu():
    print("".center(60, "*"))
    print("MENÚ".center(60, " "))
    print("".center(60, "*"))
    print("1) Empresa")
    print("2) Cliente")
    print("3) Salir")
    
def menu_emp():
    print("".center(60, "*"))
    print("BIENVENIDO AL MENU DE LA EMPRESA".center(60, " "))
    print("".center(60, "*"))
    print("1) Ingresar productos")
    print("2) Mostrar reporte")
    print("3) Salir")

def menu_cliente():
    print("".center(60, "*"))
    print("BIENVENIDO A HIMALAYA'S STORE".center(60," "))
    print("".center(60, "*"))
    print("1) Comprar producto")
    print("2) Salir")


lista_productos = []
while True:
    menu()
    opc = int(input("Ingrese una opcion: "))
    if opc == 1:
        while True:
            menu_emp()
            opc_empre = int(input("Ingrese una opción: "))
            if opc_empre == 1:
                producto = Generador_Reporte()
                lista = producto.Almacen(lista_productos)
            elif opc_empre == 2:
                producto.Mostrar_Almacen()
                producto.Muestra_reporte()
            elif opc_empre == 3:
                break
    elif opc == 2:
        while True:
            menu_cliente()
            opc_client = int(input("ingrese una opcion: "))
            if opc_client == 1:
                producto.Mostrar_Almacen()
                producto.Pedido_Cliente(lista)
                producto.reporte()
            elif opc_client == 2:
                break
    elif opc == 3:
        break
