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
        print("".center(60, "*"))
        print("INVENTARIO".center(60))
        print("".center(60, "*"))   
        print("".center(40,"-"))
        for products in self.almacen_productos:
            for x_name in ["Nombre:", "Precio:", "Cantidad:"]:
                print(x_name, products[x_name])
            print("".center(40,"-"))

class Pedido(Gestor_Inventario):
    def __init__(self):
        super().__init__()

    def Pedido_Cliente(self, Prod_disp):
        self._Prod_disp = Prod_disp
        self._n_cliente = input("ingrese su nombre: ")
        self._direccion = input("Ingrese su dirección de entrega: ")
        self.cont = 0
        cont_exist = 0
        self._precio_total = 0
        self._cantidad_total = 0
        self._precio_producto = 1
        while True:
            print("".center(60, "*"))
            print("PEDIDOS".center(60))
            print("".center(60, "*"))
            self._pedido = input("Ingrese el producto que quiere pedir: ")
            for indice, i in enumerate(self._Prod_disp):
                for j in ["Nombre:"]:
                    if self._pedido == i[j]:
                        cont_exist += 1
                        self.cont += 1
                        while True:
                            self._cantidad = int(input("Ingrese la cantidad: "))
                            if self._Prod_disp[indice]["Cantidad:"] > self._cantidad:
                                self._cantidad_total += self._cantidad
                                self._Prod_disp[indice]["Cantidad:"] -= self._cantidad
                                self._precio_producto = self._Prod_disp[indice]["Precio:"] * self._cantidad
                                self._precio_total = self._precio_total + self._precio_producto
                                break
                            else:
                                print("La cantidad ingresada supera el stock del producto...")
            if cont_exist == 0:
                print("El producto no existe...")
            print("1) Realizar otro pedido")
            print("2) Terminar pedido")
            print("3) Cancelar pedido")
            opc = int(input("Elija una opcion: "))
            if opc == 3:
                break
            elif opc == 2:
                print("".center(60, "*"))
                print("SU PEDIDO".center(60, " "))
                print("".center(60, "*"))
                print(f"Usted a elegido {self.cont} productos")
                print(f"La cantidad total es: {self._cantidad_total}")
                print("El total a pagar es: ", self._precio_total)
                break

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
