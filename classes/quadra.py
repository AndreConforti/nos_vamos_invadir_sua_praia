from datetime import datetime
from pydantic import BaseModel, Extra


class Locacao(BaseModel):
    nome_quadra: str
    min_players: int
    max_players: int

    def get_locacao_info(self):
        return f"{self.nome} é uma opção de locação."


class Quadra_BeachTenis(Locacao):
    drenagem = bool
    qtd_raquete_locacao = int

   # def __init__(self, drenagem):
   #    self.min_players = 2
   #    self.max_players = 6
   #    self.drenagem = drenagem

    def get_locacao_info(self):
        return f"A quadra de Beach Tênis '{self.nome}' atende de {self.min_players} a {self.max_players} participantes."

    def drenagem(self):
        if self.drenagem:
            return f"{self.nome} possui drenagem."
        
        return f"{self.nome} não possui drenagem"
        
class Quadra_Futebol(Locacao):
    gramado: str
    locar_bola: bool

    def get_locacao_info(self):
        if self.locar_bola:
            bola_reservada = "Bola reservada."
        else:
            bola_reservada = "Sem reserva de bola."

        return f"A quadra de Futebol '{self.nome}' atende de {self.min_players} a {self.max_players} participantes. {bola_reservada}"

'''
quadra_beachtenis = Quadra_BeachTenis.parse_obj({'nome':"Quadra 1", 'min_players': 2, 'max_players': 4, 'drenagem':False})
print (f"{quadra_beachtenis.get_locacao_info()}")
#print (f"{quadra_beachtenis.nome} atende de {quadra_beachtenis.min_players} a {quadra_beachtenis.max_players} participantes.")

quadra_futebol = Quadra_Futebol.parse_obj({'nome':"Quadra 1", 'min_players': 2, 'max_players': 4, 'gramado':'Sintético', 'locar_bola':True})
print (f"{quadra_futebol.get_locacao_info()}")
'''