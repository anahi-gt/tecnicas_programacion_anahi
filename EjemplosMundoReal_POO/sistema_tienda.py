 ======================================================
# Ejemplo del Mundo Real usando Programación Orientada a Objetos
# Caso: Sistema de una tienda en línea
# ======================================================


# ------------------------------------------------------
# Clase Producto
# Representa un producto que se vende en la tienda
# ------------------------------------------------------
class Producto:
    """
    Clase que representa un producto de la tienda.
    Cada producto tiene un nombre, un precio y una cantidad disponible (stock).
    """

    def __init__(self, nombre, precio, stock):
        # Atributos del producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def reducir_stock(self, cantidad):
        """
        Reduce el stock del producto si hay suficiente cantidad.
        Retorna True si la operación fue exitosa, False si no hay stock suficiente.
        """
        if cantidad <= self.stock:
            self.stock -= cantidad
            return True
        return False


# ------------------------------------------------------
# Clase Cliente
# Representa a un cliente que realiza compras
# ------------------------------------------------------
class Cliente:
    """
    Clase que representa a un cliente de la tienda.
    El cliente tiene un nombre y un carrito de compras.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []  # Lista de productos que el cliente desea comprar

    def agregar_al_carrito(self, producto, cantidad):
        """
        Agrega un producto y su cantidad al carrito del cliente.
        """
        self.carrito.append((producto, cantidad))


# ------------------------------------------------------
# Clase Tienda
# Representa la tienda que gestiona los productos y las compras
# ------------------------------------------------------
class Tienda:
    """
    Clase que representa la tienda.
    La tienda administra productos y procesa las compras de los clientes.
    """

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista de productos disponibles en la tienda

    def agregar_producto(self, producto):
        """
        Agrega un producto al inventario de la tienda.
        """
        self.productos.append(producto)

    def mostrar_productos(self):
        """
        Muestra todos los productos disponibles en la tienda.
        """
        print(f"\n--- Productos disponibles en {self.nombre} ---")
        for producto in self.productos:
            print(f"{producto.nombre} - Precio: ${producto.precio} - Stock: {producto.stock}")

    def procesar_compra(self, cliente):
        """
        Procesa la compra del cliente.
        Reduce el stock de los productos y calcula el total a pagar.
        """
        total = 0

        for producto, cantidad in cliente.carrito:
            if producto.reducir_stock(cantidad):
                total += producto.precio * cantidad
            else:
                print(f"No hay suficiente stock del producto: {producto.nombre}")

        print(f"\nCompra realizada por {cliente.nombre}. Total a pagar: ${total}")


# ------------------------------------------------------
# Uso del sistema (Simulación del mundo real)
# ------------------------------------------------------

# Se crea la tienda
tienda = Tienda("Tienda Online")

# Se crean productos
producto1 = Producto("Celular Samsung", 800, 5)
producto2 = Producto("Audifonos", 20, 10)

# Se agregan los productos a la tienda
tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)

# Se crea un cliente
cliente = Cliente("Anahi")

# El cliente agrega productos a su carrito
cliente.agregar_al_carrito(producto1, 1)
cliente.agregar_al_carrito(producto2, 2)

# Se muestran los productos disponibles
tienda.mostrar_productos()

# Se procesa la compra del cliente
tienda.procesar_compra(cliente)
