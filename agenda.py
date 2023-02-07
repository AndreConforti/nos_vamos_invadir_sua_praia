from quadra import Quadra
from datetime import datetime, timedelta
import csv

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
            if quadra.agendar(data, hora_inicio, hora_fim):
                quadras_disponiveis.append(quadra)
        return quadras_disponiveis


    def confirmar_reserva(self, cliente, data, hora_inicio, hora_fim):
        disponiveis = self.verificar_disponibilidade(data, hora_inicio, hora_fim)
        if len(disponiveis) == 0:
            print('Desculpe não há quadras disponíveis nesse horário')
            return False
        
        print('Quadras disponíveis:')
        for i, quadra in enumerate(disponiveis):
            print(f'{i + 1} - {quadra}')

        escolha = int(input('Escolha a quadra (digite o número): '))
        quadra = disponiveis[escolha - 1]

        confirmacao = input(f'Deseja reservar a quadra {quadra} para o dia {data} das {hora_inicio} às {hora_fim}? (s/n)').upper()[0]
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


    def consultar_reservas_duplicadas(self, quadra, data, hora_inicio, hora_fim):
        lista = self.recuperar_reservas()
        for item in lista:
            if (quadra in item['quadra']) and (data in item['data']) and (hora_inicio in item['hora_inicio']) and (hora_fim in item['hora_fim']):
                print("Não será possível agendar nessa data e horário")
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

  