from abc import ABC, abstractmethod
from typing import List

# Clase abstracta Producto
class Producto(ABC):
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    @abstractmethod
    def mostrar_detalles(self):
        pass

    def actualizar_cantidad(self, cantidad: int):
        self.cantidad += cantidad

# Clases concretas para cada tipo de producto

class Electrodomestico(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, voltaje: str):
        super().__init__(nombre, precio, cantidad)
        self.voltaje = voltaje

    def mostrar_detalles(self):
        return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad} - Voltaje: {self.voltaje}"

class Alimento(Producto):
    def __init__(self, nombre: str, precio: float, cantidad: int, fecha_expiracion: str):
        super().__init__(nombre, precio, cantidad)
        self.fecha_expiracion = fecha_expiracion

    def mostrar_detalles(self):
        return f"{self.nombre} - Precio: ${self.precio} - Cantidad: {self.cantidad} - Fecha de expiración: {self.fecha_expiracion}"

# Interfaz Inventario
class Inventario(ABC):
    @abstractmethod
    def agregar_producto(self, producto: Producto):
        pass

    @abstractmethod
    def quitar_producto(self, nombre: str, cantidad: int):
        pass

    @abstractmethod
    def mostrar_inventario(self):
        pass

# Implementación de Inventario
class InventarioConcreto(Inventario):
    def __init__(self):
        self.productos: List[Producto] = []

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)

    def quitar_producto(self, nombre: str, cantidad: int):
        for producto in self.productos:
            if producto.nombre == nombre:
                if producto.cantidad >= cantidad:
                    producto.actualizar_cantidad(-cantidad)
                    print(f"Se ha quitado {cantidad} unidades de {nombre}.")
                    return
                else:
                    print(f"No hay suficientes unidades de {nombre}.")
                    return
        print(f"Producto {nombre} no encontrado en el inventario.")

    def mostrar_inventario(self):
        for producto in self.productos:
            print(producto.mostrar_detalles())

# Crear productos
producto1 = Electrodomestico("Televisor", 500.0, 10, "110V")
producto2 = Alimento("Arroz", 2.5, 50, "2025-12-31")

# Crear inventario y agregar productos
inventario = InventarioConcreto()
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

# Mostrar inventario
print("Inventario:")
inventario.mostrar_inventario()

# Quitar productos
inventario.quitar_producto("Televisor", 2)

# Mostrar inventario después de quitar productos
print("\nInventario después de quitar productos:")
inventario.mostrar_inventario()
