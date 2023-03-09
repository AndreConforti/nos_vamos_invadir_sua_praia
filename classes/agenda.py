# Importa a classe Quadra
import csv
import pdb

from classes.quadra import Quadra_BeachTenis
from classes.reserva import Reserva
from classes.cliente import Cliente
from typing import List
from pydantic import BaseModel, Extra
from datetime import date, datetime
from logger import Logger

#from cpf_generator import generate_cpf

# Cria uma classe chamada Agenda
class Agenda(BaseModel):
    reservas: list[Reserva] = []
    quadras: list[Quadra_BeachTenis] = [
            Quadra_BeachTenis.parse_obj({'nome_quadra':'Quadra 1', 'min_players':2, 'max_players':4, 'drenagem':True}),
            Quadra_BeachTenis.parse_obj({'nome_quadra':'Quadra 2', 'min_players':2, 'max_players':4, 'drenagem':True}),
            Quadra_BeachTenis.parse_obj({'nome_quadra':'Quadra 3', 'min_players':2, 'max_players':4, 'drenagem':True}),
            Quadra_BeachTenis.parse_obj({'nome_quadra':'Quadra 4', 'min_players':2, 'max_players':4, 'drenagem':True})
        ]
    
    class Config:
        extra = 'allow'

    def get_reservas(self):
        """fake = Faker()

        # Simula uma base inicial
        #_cpf = generate_cpf()
        try:
            cliente = Cliente(nome='Julay',cpf='1111111112',telefone='999888999',email='a@b.com')
        except ValueError as e:
            print(str(e).replace('(type=value_error)', ''))
            return
        
        quadra = self.quadras[0]

        _date=date.fromisoformat('2023-03-07')  
        try:
            reserva1 = Reserva(cliente=cliente,quadra=quadra, data=_date, hora_inicio = 10, duracao = 3)
            reserva2 = Reserva(cliente=cliente,quadra=quadra, data=_date, hora_inicio = 15, duracao = 1)
        except ValueError as e:
            print(str(e).replace('(type=value_error)', ''))
            return
        
        self.reservas.append(reserva1)
        self.reservas.append(reserva2)
        """
        try:
            with open("files/agenda.csv", newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for registro in reader:
                    #breakpoint()
                    cliente = Cliente(nome=registro["nome"],cpf=registro["cpf"],telefone=registro["telefone"],email=registro["email"])
                    quadra = Quadra_BeachTenis(nome_quadra=registro["nome_quadra"], min_players=registro["min_players"], max_players=registro["max_players"])
                    if registro["data_pago"] == '':
                        data_pago = None
                    else:
                        data_pago = registro["data_pago"]
                    reserva = Reserva(cliente=cliente, quadra=quadra, data=registro["data"], hora_inicio=registro["hora_inicio"], duracao=registro["duracao"], data_pago=data_pago)
                    self.reservas.append(reserva)
        except FileNotFoundError:
            pass    # Ok não existir arquivo inicialmente
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   

        # preserva variáveis iniciais da classe. No caso, uma lista de quadras com 3 dados
        # - Nome da Quadra
        # - Hora Início (dias da semana)
        # - Hora Fim (dias da semana)
        # - Obs: se ao criar a instância da classe já definimos automaticamente domingo, pq não os demais dias?
        #

        # Carregar da base toda a agenda definida
        self.get_reservas()
        
    # 
    def agendar(self, cliente, data, hora_ini, duracao):
        logger = Logger()

        quadras = self.quadra_disponivel (data, hora_ini, duracao)
        logger.log('debug', '----------------------------------------------------------------')
        if not quadras:
            # TODO: retorna erro?
            return []
        
        try:
            reserva = Reserva(cliente=cliente, quadra=quadras[0], data=data, hora_inicio=hora_ini, duracao = duracao)
        except ValueError as e:
            logger.log('warning', (str(e)))
            return []
        
        self.reservas.append(reserva)
        return quadras[0]
    

    # Salva a agenda ao encerrar sistema
    def save_agenda(self):
        # Gravando agenda
        fieldnames = list(Cliente.__fields__.keys())
        fieldnames.extend(list(Quadra_BeachTenis.__fields__.keys()))
        fieldnames.extend(["data", "hora_inicio", "duracao", "data_pago"])
        with open("files/agenda.csv", "w", newline="") as arquivo:
            writer = csv.DictWriter(arquivo, fieldnames=fieldnames)
            writer.writeheader()
            for reserva in self.reservas:
                registro = dict()
                 
                registro["nome"] = reserva.cliente.nome
                registro["cpf"] = reserva.cliente.cpf
                registro["telefone"] = reserva.cliente.telefone
                registro["email"] = reserva.cliente.email
                registro["nome_quadra"] = reserva.quadra.nome_quadra
                registro["min_players"] = reserva.quadra.min_players
                registro["max_players"] = reserva.quadra.max_players
                registro["data"] = reserva.data
                registro["hora_inicio"] = reserva.hora_inicio
                registro["duracao"] = reserva.duracao
                registro["data_pago"] = reserva.data_pago

                # breakpoint()
                writer.writerow(registro)


    # Método para checar as reservas 
    def quadra_disponivel(self, data, hora_inicio, duracao):
        logger = Logger()
        quadras_disponiveis = []
        hora_inicio = int(hora_inicio)
        hora_fim = hora_inicio + int(duracao)
        logger.log('debug', f'Buscando dia {data} das {hora_inicio} até as {hora_fim}')

        # TODO: validar valores fornecidos

        for quadra in self.quadras:
            logger.log('debug', f'Checando quadra {quadra.nome_quadra}')
            quadra_livre = True
            for reserva_vig in self.reservas:
                # Hora Inicio < Fim e Hora Fim > inicio 
                if (quadra.nome_quadra == reserva_vig.quadra.nome_quadra \
                    and data == reserva_vig.data \
                    and hora_inicio <= int(reserva_vig.hora_fim()) 
                    and hora_fim >= reserva_vig.hora_inicio):
                    logger.log('warning', f'Quadra {quadra.nome_quadra} não está disponível')
                    logger.log('warning', f'{reserva_vig.data} {reserva_vig.hora_inicio} {reserva_vig.hora_fim()}')
                    quadra_livre = False
                    break
            
            if quadra_livre:
                logger.log('debug', f'Quadra {quadra.nome_quadra} está disponível')
                quadras_disponiveis.append(quadra)
                
        return quadras_disponiveis
    
    # Método para criar nova reserva
    def reservas_cliente(self, nome_cpf):
        logger = Logger()
        reservas_cliente = []
        
        # TODO: validar valores fornecidos

        logger.log('debug', f'Buscando cliente com nome ou CPF igual a {nome_cpf}')        
        for reserva_vig in self.reservas:
            # Hora Inicio < Fim e Hora Fim > inicio 
            if (nome_cpf == reserva_vig.cliente.nome or nome_cpf == reserva_vig.cliente.cpf):
                logger.log('debug', f'Reserva: {reserva_vig}')
                reservas_cliente.append(reserva_vig)
                
        return reservas_cliente

    def cancelar_reserva(self, data, hora_inicio):
        logger = Logger()
        reserva = []

        date_obj = datetime.strptime(data, "%Y-%m-%d")
        try:
            hora_inicio = int(hora_inicio)
        except ValueError as e:
            logger.log('warning', (str(e)))
            return []

        for i, registro in enumerate(self.reservas):  # É preciso passar índice e valor, pois o método pop elimina o índice
            #pdb.set_trace()
            if (date_obj.date() == registro.data and hora_inicio == registro.hora_inicio):
                reserva = registro
                self.reservas.pop(i)
                logger.log('debug', f"Reserva excluída com sucesso!")
                break
            else:
                print(f"{registro.data}/{date_obj.date()} - {registro.hora_inicio}/{hora_inicio}")

        return reserva
    
    def pagar_reserva(self, data, hora_inicio, data_pago):
        logger = Logger()
        reserva = []

        date_obj = datetime.strptime(data, "%Y-%m-%d")
        try:
            hora_inicio = int(hora_inicio)
        except ValueError as e:
            logger.log('warning', (str(e)))
            return []

        for i, registro in enumerate(self.reservas):  # É preciso passar índice e valor, pois o método pop elimina o índice
            #pdb.set_trace()
            if (date_obj.date() == registro.data and hora_inicio == registro.hora_inicio):
                reserva = registro
                registro.data_pago = data_pago
                logger.log('debug', f"Reserva paga com sucesso!")
                break
           # else:
                #print(f"{registro.data}/{date_obj.date()} - {registro.hora_inicio}/{hora_inicio}")

        return reserva

# ====================================================
#if __name__ == '__main__':
#    
#    agenda = Agenda()
#
#    disponivel = agenda.verificar_disponibilidade('2023-02-07', 11, 12, 1)
#
#    if disponivel == []:
#        print("Nenhuma quadra disponível")
#    else:
#        for quadra in disponivel:
#            print(quadra.nome_quadra)


    
