from typing import List, Optional, Dict
from ..models.producto import Producto 
from .i_repositorio import IRepositorio

class RepositorioMemoria(IRepositorio):

    def __init__(self, **kwargs): # Añadir **kwargs para evitar error si RepositorioMemoria es llamado sin argumentos
        self._productos: Dict[int, Producto] = {}

    # (Continúa con el resto de los métodos: agregar, obtener, etc.)
    # ... tal como se ve en tu imagen
    
    def agregar(self, producto: Producto) -> bool:
        # ... lógica de agregar ...
        pass # Placeholder for actual implementation
    
