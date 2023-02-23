from datetime import datetime
from pydantic import BaseModel, Extra

class Quadra(BaseModel):
    nome: str
    horarios:dict= {'0' : {'ini': 0, 'fim' : 0}, # Horários, sendo Segunda = 0 e Domingo = 6
            '1' : {'ini': 10, 'fim' : 22}, 
            '2' : {'ini': 10, 'fim' : 22}, 
            '3' : {'ini': 10, 'fim' : 22}, 
            '4' : {'ini': 10, 'fim' : 22}, 
            '5' : {'ini': 10, 'fim' : 22}, 
            '6' : {'ini': 9, 'fim' : 18}}

  #  def __init__(self):
    #    asser
        

    def __str__(self):
        return str(self.nome)

    # Método para consultar disponibilidade de agendamento
    """
        Obs: se vamos trabalhar com duração, porque precisa indicar a hora_fim? 
        Não seria a hora inicio + duracao-1?
    """
    def agendar(self, data, hora_inicio, hora_fim, duracao):

        # trata as variáveis fornecidas
        data = datetime.strptime(data, '%Y-%m-%d').date()   # Extrai a data da string
        hora_inicio = int(hora_inicio) # Ignora decimais para definição da hora
        ###hora_fim = int(hora_fim) # Ignora decimais para definição da hora
        duracao = int(duracao) # Ignora decimais para definição da duração
        
        # Verifica se é uma duração válida
        if duracao not in [1, 3]:
            return False

        hora_fim = hora_inicio + duracao - 1 # Calcula a hora_fim conforme duração escolhida
        dia_semana = data.weekday() # Identifica o dia da semana

        """
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
        """
            
        if hora_inicio < self.horarios[dia_semana]['ini'] or hora_fim > self.horarios[dia_semana]['fim']:
            return False
        
        hora_atual = hora_inicio

        # Obs: pela regra calculada acima, este cálculo não é mais necessário:
        #if (hora_fim - hora_atual) % 2 == 0:
        #    return False

        # Se não existe nenhuma agenda disponível, inicia zerada
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