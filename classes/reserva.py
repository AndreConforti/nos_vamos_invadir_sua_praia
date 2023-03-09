from pydantic import BaseModel, validator
from classes.cliente import Cliente
from classes.quadra import Quadra_BeachTenis
from datetime import date

class Reserva(BaseModel):
    arbitrary_types_allowed = True    
    cliente : Cliente
    quadra : Quadra_BeachTenis    
    hora_inicio : int
    duracao : int
    data : date
    data_pago : date = None
    
    error_msg_templates = {}

    class Config:
        validate_assignment = True
    
    @validator('data')
    def valida_hora(cls, v, values):

        horarios = {'0' : {'dia': 'Às Segundas', 'ini': 0, 'fim' : 0}, # Horários, sendo Segunda = 0 e Domingo = 6
            '1' : {'dia': 'Às Terças', 'ini': 10, 'fim' : 22}, 
            '2' : {'dia': 'Às Quartas', 'ini': 10, 'fim' : 22}, 
            '3' : {'dia': 'Às Quintas', 'ini': 10, 'fim' : 22}, 
            '4' : {'dia': 'Às Sextas', 'ini': 10, 'fim' : 22}, 
            '5' : {'dia': 'Aos Sábados', 'ini': 10, 'fim' : 22}, 
            '6' : {'dia': 'Aos Domingos', 'ini': 9, 'fim' : 18}}
        
        #breakpoint()

       # if v < date.today():
    #    raise ValueError('Data precisa ser igual ou superior a hoje')
        
        if values['duracao'] not in [1, 3]:
            raise ValueError('Duração permitida é de 1 ou 3 horas, respeitando o horário de término do dia.')
        
        if v.weekday() == 0:
            raise ValueError('Quadras não operam de segunda-feira.')
        
        if values['hora_inicio'] < horarios[str(v.weekday())]['ini']:
            raise ValueError(f"{horarios[str(v.weekday())]['dia']}, horário de funcionamento é das {horarios[str(v.weekday())]['ini']} às {horarios[str(v.weekday())]['fim']} horas.")
        
        # TODO: concluir validadores (hora_fim)
        return v

    def hora_fim(self):
       return self.hora_inicio + self.duracao
    

    def valor_reserva(self):
        if self.duracao == 1:
            return 100
        
        return 250



    