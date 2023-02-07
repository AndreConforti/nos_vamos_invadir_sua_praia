from datetime import datetime


class HorarioForaDoFuncionamento(Exception):
    pass


class Quadra:

    def __init__(self, nome, hora_inicio, hora_fim, hora_inicio_domingo='09', hora_fim_domingo='18'):
        self.nome = nome
        self.hora_inicio = int(hora_inicio)
        self.hora_fim = int(hora_fim)
        self.hora_inicio_domingo = int(hora_inicio_domingo)
        self.hora_fim_domingo = int(hora_fim_domingo)


    def __str__(self):
        return str(self.nome)


    def agendar(self, data, hora_inicio, hora_fim):
        data = datetime.strptime(data, '%Y-%m-%d').date()
        hora_inicio = int(hora_inicio)
        hora_fim = int(hora_fim)
        
        if data.weekday() == 6:  # Domingo
            hora_inicio_disponivel = self.hora_inicio_domingo
            hora_fim_disponivel = self.hora_fim_domingo
            
        elif data.weekday() == 0:  # Segunda
            raise HorarioForaDoFuncionamento('Estabelecimento fechado nesta data')

        else:
            hora_inicio_disponivel = self.hora_inicio
            hora_fim_disponivel = self.hora_fim
            data = datetime.strftime(data, "%Y-%m-%d")
            duracao = hora_fim - hora_inicio

        if hora_inicio < hora_inicio_disponivel or hora_fim > hora_fim_disponivel:
            raise HorarioForaDoFuncionamento("O horário fornecido está fora do horário de funcionamento")

        if duracao not in [1, 3]:
            raise HorarioForaDoFuncionamento("O período deve ser de 1 ou 3 horas")

        hora_atual = hora_inicio

        if (hora_fim - hora_atual) % 2 == 0:
            raise HorarioForaDoFuncionamento("O período deve ser de 1 ou 3 horas")

        return True


