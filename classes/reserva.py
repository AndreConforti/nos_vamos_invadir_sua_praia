from pydantic import BaseModel
from classes.cliente import Cliente
from classes.quadra import Quadra
from datetime import datetime

class Reserva(BaseModel):
    arbitrary_types_allowed = True    
    cliente : Cliente
    quadra : Quadra
    data : str
    hora_inicio : int
    duracao : int
    
    def hora_fim(self):
       return self.hora_inicio + self.duracao



    