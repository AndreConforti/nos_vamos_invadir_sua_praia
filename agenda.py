from quadra import Quadra
from cliente import Cliente

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
            return True
        else:
            print("Reserva cancelada!")
            return False

# ====================================================
if __name__ == '__main__':
    
    agenda = Agenda()

    disponivel = agenda.verificar_disponibilidade('2023-02-07', '14', '15', '1')

    if disponivel == []:
        print("Nenhuma quadra dispinível")
    else:
        for quadra in disponivel:
            print(quadra.nome)


    
