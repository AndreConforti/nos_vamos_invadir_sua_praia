from datetime import datetime


class Quadra:

    def __init__(self, nome, hora_inicio, hora_fim, hora_inicio_domingo='09', hora_fim_domingo='18'):
        self.nome = nome
        self.hora_inicio = int(hora_inicio)
        self.hora_fim = int(hora_fim)
        self.hora_inicio_domingo = int(hora_inicio_domingo)
        self.hora_fim_domingo = int(hora_fim_domingo)
        self.agenda = {}


    def __str__(self):
        return str(self.nome)


    def agendar(self, data, hora_inicio, hora_fim, duracao):
        data = datetime.strptime(data, '%Y-%m-%d').date()
        hora_inicio = int(hora_inicio)
        hora_fim = int(hora_fim)
        duracao = int(duracao)
        
        if data.weekday() == 6:  # Domingo
            hora_inicio_disponivel = self.hora_inicio_domingo
            hora_fim_disponivel = self.hora_fim_domingo
            
        elif data.weekday() == 0:  # Segunda
            return False
        else:
            hora_inicio_disponivel = self.hora_inicio
            hora_fim_disponivel = self.hora_fim
            data = datetime.strftime(data, "%Y-%m-%d")

        if hora_inicio < hora_inicio_disponivel or hora_fim > hora_fim_disponivel:
            return False

        if duracao not in [1, 3]:
            return False

        hora_atual = hora_inicio

        if (hora_fim - hora_atual) % 2 == 0:
            return False

        if data not in self.agenda:
            self.agenda[data] = []

        while hora_atual < hora_fim:
            if data in self.agenda and hora_atual in self.agenda[data]:
                return False
            self.agenda[data].append(hora_atual)
            hora_atual += 1 if duracao == 3 else 3
        return True



# ======================================================================
if __name__ == '__main__':

    quadra = Quadra('Quadra 1', '10', '22')
    teste = quadra.agendar('2023-02-07', 14, 15, 1)
    print(teste)
    print(quadra.nome, quadra.agenda)