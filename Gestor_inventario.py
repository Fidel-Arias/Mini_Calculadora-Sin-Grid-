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
                        self._cantidad = int(input("Ingrese la cantidad: "))
                        self._cantidad_total += self._cantidad
                        self._Prod_disp[indice]["Cantidad:"] -= self._cantidad
                        self._precio_producto = self._Prod_disp[indice]["Precio:"] * self._cantidad
                        self._precio_total = self._precio_total + self._precio_producto
            if cont_exist == 0:
                print("El producto no existe...")
            print("1) Realizar otro pedido")
            print("2) Terminar pedido")
            print("3) Cancelar pedido")
            opc = int(input("Elija una opcion: "))
            if opc == 3:
                break
            elif opc == 2:
                print(f"Usted a elegido {self.cont} productos")
                print(f"La cantidad total es: {self._cantidad_total}")
                print("El total a pagar es: ", self._precio_total)
                break


class Generador_Reporte(Pedido):
    def vender(self):
        if self.cont > self._cantidad:
            print("No hay suficiente stock para realizar la venta.")
        else:
            self._cantidad -= self.cont
            ganancias = self._precio * self.cont
            self.ganancias += ganancias
            print("Se vendieron ", self.cont, "en total")
            print("Stock restante: ", self._cantidad, ".")
            print("Ganancias totales: $", self.ganancias, ".")


lista_productos = []
for i in range(2):
    producto = Pedido()
    lista = producto.Almacen(lista_productos)
    if i == 1:
        producto.Mostrar_Almacen()
        producto.Pedido_Cliente(lista)
        producto.Mostrar_Almacen()
        reporte = Generador_Reporte()
        reporte.vender()
        break
