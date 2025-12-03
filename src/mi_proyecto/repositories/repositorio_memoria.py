from typing import List, Optional, Dict
from ..models.producto import Producto 
from .i_repositorio import IRepositorio

class RepositorioMemoria(IRepositorio):

    def __init__(self, **kwargs): 
        self._productos: Dict[int, Producto] = {}

   
    
    def agregar(self, producto: Producto) -> bool:
       
        pass 
    
