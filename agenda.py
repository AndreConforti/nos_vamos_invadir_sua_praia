from quadra import Quadra


class Agenda:
    def __init__(self):
        self.quadras = [
            Quadra('Quadra 1', '10', '22'),
            Quadra('Quadra 2', '10', '22'),
            Quadra('Quadra 3', '10', '22'),
            Quadra('Quadra 4', '10', '22'),
        ]

    def verificar_disponibilidade(self, data, hora_inicio, hora_fim, duracao):
        quadras_disponiveis = []
        for quadra in self.quadras:
            if quadra.agendar(data, hora_inicio, hora_fim, duracao):
                quadras_disponiveis.append(quadra)
        return quadras_disponiveis




# ====================================================
if __name__ == '__main__':
    
    agenda = Agenda()

    disponivel = agenda.verificar_disponibilidade('2023-02-07', 11, 12, 1)

    if disponivel == []:
        print("Nenhuma quadra dispinível")
    else:
        for quadra in disponivel:
            print(quadra.nome)


    
