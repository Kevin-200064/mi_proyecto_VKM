from abc import ABC, abstractmethod
from typing import List, Optional, Dict

# --- MODELOS ---

class Categoria:
    MEDICAMENTOS = "Medicamentos"
    HIGIENE = "Higiene"
    PRIMEROS_AUXILIOS = "Primeros Auxilios"

class Producto:
    _next_id = 1
    def __init__(self, nombre: str, descripcion: str, precio: float, cantidad: int, categoria: Categoria):
        self.id_producto = Producto._next_id
        Producto._next_id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria

    def actualizar_cantidad(self, nueva_cantidad: int):
        self.cantidad = nueva_cantidad

# --- INTERFAZ IRepositorio (Capa de Datos - Contrato) ---
class IRepositorio(ABC):
    
    @abstractmethod
    def agregar(self, producto: Producto) -> bool:
        pass
    @abstractmethod
    def obtener(self, id_producto: int) -> Optional[Producto]:
        pass
    @abstractmethod
    def obtener_todos(self) -> List[Producto]:
        pass
    @abstractmethod
    def eliminar(self, id_producto: int) -> bool:
        pass

