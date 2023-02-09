from quadra import Quadra
from datetime import datetime, timedelta
import csv

class HorarioForaDoFuncionamento(Exception):
    pass

class ReservaDuplicada(Exception):
    pass 


class Agenda:
    def __init__(self):
        self.quadras = [
            Quadra('Quadra 1', '10', '22'),
            Quadra('Quadra 2', '10', '22'),
            Quadra('Quadra 3', '10', '22'),
            Quadra('Quadra 4', '10', '22'),
        ]
        self.reservas = []


    def verificar_disponibilidade(self, data, hora_inicio, hora_fim):
        quadras_disponiveis = []
        for quadra in self.quadras:
            if self.consultar_reservas_duplicadas(quadra.nome, data, hora_inicio):
                quadras_disponiveis.append(quadra)
        return quadras_disponiveis


    def confirmar_reserva(self, quadras, cliente, data, hora_inicio, hora_fim):
        disponiveis = self.verificar_disponibilidade(data, hora_inicio, hora_fim)
        if len(disponiveis) == 0:
            print('Desculpe não há quadras disponíveis nesse horário')
            return False

        data = datetime.strptime(data, '%Y-%m-%d').date()
        hora_inicio = int(hora_inicio)
        hora_fim = int(hora_fim)
        
        if data.weekday() == 6:  # Domingo
            hora_inicio_disponivel = self.hora_inicio_domingo
            hora_fim_disponivel = self.hora_fim_domingo
            
        elif data.weekday() == 0:  # Segunda
            raise HorarioForaDoFuncionamento('Estabelecimento fechado nesta data')

        else:
            for indice in quadras:
                hora_inicio_disponivel = quadras[indice].hora_inicio
                hora_fim_disponivel = quadras[indice].hora_fim
                # data = datetime.strftime(data, "%Y-%m-%d")
                duracao = hora_fim - hora_inicio
                duracao = int(duracao)

        if hora_inicio < hora_inicio_disponivel or hora_fim > hora_fim_disponivel:
            raise HorarioForaDoFuncionamento("O horário fornecido está fora do horário de funcionamento")

        if duracao not in [1, 3]:
            raise HorarioForaDoFuncionamento("O período deve ser de 1 ou 3 horas")

        hora_atual = hora_inicio

        if (hora_fim - hora_atual) % 2 == 0:
            raise HorarioForaDoFuncionamento("O período deve ser de 1 ou 3 horas")

        print('Quadras disponíveis:')
        for i, quadra in enumerate(disponiveis):
            print(f'{i + 1} - {quadra}')

        escolha = int(input('Escolha a quadra (digite o número): '))
        quadra = disponiveis[escolha - 1]
        print(disponiveis)
            
        confirmacao = input(f'Deseja reservar a quadra {quadra.nome} para o dia {data} das {hora_inicio} às {hora_fim}? (s/n)').upper()[0]
        if confirmacao == 'S':
            reserva = {
                'cliente'    : cliente,
                'quadra'     : str(quadra.nome),
                'data'       : data,
                'hora_inicio': hora_inicio,
                'hora_fim'   : hora_fim 
            }
            self.reservas.append(reserva)
            print("Reserva realizada com sucesso!")
            self.gravar_reservas()
            return True
        else:
            print("Reserva cancelada!")
            return False



    def gravar_reservas(self, filename='reservas.csv'):
        reservas = self.reservas
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['cliente', 'quadra', 'data', 'hora_inicio', 'hora_fim']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for reserva in reservas:
                writer.writerow(reserva)


    def recuperar_reservas(self, filename='reservas.csv'):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile)
            reservas = [row for row in reader]
            return reservas


    def consultar_cliente(self, cliente):
        lista = self.recuperar_reservas()
        for item in lista:
            if cliente in item.values():
                print(item)


    def consultar_reservas_duplicadas(self, quadra, data, hora_inicio):
        lista = self.recuperar_reservas()
        for item in lista:
            if (quadra in item['quadra']) and (str(data) in item['data']) and (str(hora_inicio) in item['hora_inicio']):
                return False
        return True


    def cancelar_reserva(self, cliente, quadra, data, hora_inicio, hora_fim):
        reserva_encontrada = None
        reservas = self.recuperar_reservas()
        for reserva in reservas:
            if (reserva['cliente'] == cliente) and (reserva['quadra'] == quadra) and (reserva['data'] == data) and (reserva['hora_inicio'] == hora_inicio) and (reserva['hora_fim'] == hora_fim):
                reserva_encontrada = reserva
                break

        if reserva_encontrada:
            hora_limite_cancelamento = int(reserva_encontrada['hora_inicio']) - 3
            agora = str(datetime.now())
            if hora_limite_cancelamento < int(agora[11:13]):
                print('Não é possível cancelar a reserva. O limite é de 3 horas antes do horário início')
                return False

            confirmacao = input(f'Deseja cancelar a reserva? (s/n)').upper()[0]
            if confirmacao == 'S':
                reservas.remove(reserva_encontrada)
                print("Reserva cancelada com sucesso!")
                self.reservas = reservas
                self.gravar_reservas()
                return True
            else:
                print('OK. A reserva não foi cancelada')        
        
        else:
            print('Não há nenhuma reserva para esse cliente nessas condições')
            return False

  