# Importa a classe Quadra
from classes.quadra import Quadra
from classes.reserva import Reserva
from classes.cliente import Cliente
from pydantic import BaseModel, Extra
from datetime import datetime
from logger import Logger
from faker import Faker
#from cpf_generator import generate_cpf

# Cria uma classe chamada Agenda
class Agenda(BaseModel):
    reservas: list[Reserva] = []
    quadras: list[Quadra] = [
            Quadra(nome='Quadra 1'),
            Quadra(nome='Quadra 2'),
            Quadra(nome='Quadra 3'),
            Quadra(nome='Quadra 4')
        ]

    class Config:
        extra = 'allow'


    def get_reservas(self):
        fake = Faker()

        # Simula uma base inicial
        #_cpf = generate_cpf()
        cliente = Cliente(nome='Julay',cpf='1111111112',telefone='999888999',email='a@b.com')
        quadra = Quadra(nome='Quadra 1')

        date=datetime.strptime('2023-02-01', '%Y-%m-%d').date
        reserva1 = Reserva(cliente=cliente,quadra=quadra, data='2023-02-01', hora_inicio = 10, duracao = 3)
        reserva2 = Reserva(cliente=cliente,quadra=quadra, data='2023-02-01', hora_inicio = 15, duracao = 1)
        self.reservas.append(reserva1)
        self.reservas.append(reserva2)

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
        
        reserva = Reserva(cliente=cliente, quadra=quadras[0], data=data, hora_inicio=hora_ini, duracao = duracao)
        self.reservas.append(reserva)
        return quadras[0]
    

    # Método para checar as reservas 
    def quadra_disponivel(self, data, hora_inicio, duracao):
        logger = Logger()
        quadras_disponiveis = []
        hora_inicio = int(hora_inicio)
        hora_fim = hora_inicio + int(duracao)
        logger.log('debug', f'Buscando dia {data} das {hora_inicio} até as {hora_fim}')

        # TODO: validar valores fornecidos

        for quadra in self.quadras:
            logger.log('debug', f'Checando quadra {quadra.nome}')
            quadra_livre = True
            for reserva_vig in self.reservas:
                # Hora Inicio < Fim e Hora Fim > inicio 
                if (quadra.nome == reserva_vig.quadra.nome \
                    and data == reserva_vig.data \
                    and hora_inicio <= int(reserva_vig.hora_fim()) 
                    and hora_fim >= reserva_vig.hora_inicio):
                    logger.log('warning', f'Quadra {quadra.nome} não está disponível')
                    logger.log('warning', f'{reserva_vig.data} {reserva_vig.hora_inicio} {reserva_vig.hora_fim()}')
                    quadra_livre = False
                    break
            
            if quadra_livre:
                logger.log('debug', f'Quadra {quadra.nome} está disponível')
                quadras_disponiveis.append(quadra)
                
        return quadras_disponiveis
    
    # Método para criar nova reserva
    def reservas_cliente(self, nome):
        logger = Logger()
        reservas_cliente = []
        #hora_inicio = int(hora_inicio)
        #hora_fim = hora_inicio + int(duracao)
        
        # TODO: validar valores fornecidos

        print('Buscando cliente ', nome)        
        for reserva_vig in self.reservas:
            # Hora Inicio < Fim e Hora Fim > inicio 
            if (nome == reserva_vig.cliente.nome):
                logger.log('debug', f'Reserva: {reserva_vig}')
                reservas_cliente.append(reserva_vig)
                
        return reservas_cliente


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
#            print(quadra.nome)


    
