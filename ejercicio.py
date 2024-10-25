class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre 
        self.precio = precio  
        self.cantidad = cantidad  

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.cantidad}")
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla) :
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
class Inventario:
    def __init__(self):
        self.prendas = []

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()
class Tienda:
    def __init__(self):
        self.inventario = Inventario()

    def agregar_producto(self, prenda):
        self.inventario.agregar_prenda(prenda)

    def mostrar_productos(self):
        self.inventario.mostrar_inventario()

