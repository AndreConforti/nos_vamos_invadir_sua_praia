from classes.reserva import Reserva
from classes.cliente import Cliente
from classes.quadra import Quadra
from datetime import datetime


def get_distinct_values(lst):
    return set(lst)

reservas = []
cliente = Cliente(nome='Julay',cpf='1111',telefone='999-999',email='a@b.com')
quadra = Quadra(nome='Quadra 1')

date_string = '2023-02-01'
date_format = '%Y-%m-%d'
date = datetime.strptime(date_string, date_format)

reserva1 = Reserva(cliente=cliente,quadra=quadra, data=date, hora_inicio = 10, duracao = 3)
reserva2 = Reserva(cliente=cliente,quadra=quadra, data=date, hora_inicio = 15, duracao = 3)
reservas.append(reserva1)
reservas.append(reserva2)

testeQuadra = Quadra(nome='Quadra 1')

if testeQuadra not in reservas:
    print ('Ok')
else:
    print ('Tá')



#
#from pydantic import BaseModel
#
#class Cliente(BaseModel):
#    nome: str
#    idade: int
#    endereco: str
#
#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.full_name = f"{self.nome} ({self.idade})"
#
#cliente = Cliente(nome="John Doe", idade=30, endereco="123 Main St.")
#
## Access the full_name attribute, which was set up in the __init__ method
#print(cliente.full_name)  # Output: John Doe (30)
