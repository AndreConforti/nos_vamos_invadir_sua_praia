from agenda import Agenda
from quadra import Quadra, HorarioForaDoFuncionamento
from cliente import Cliente


cliente = Cliente(
    nome='Andre Conforti',
    cpf='278.759.698-32',
    telefone='19 98837-7497',
    email='andre.conforti@gmail.com'
)

quadra1 = Quadra(nome='Quadra 1', hora_inicio='10', hora_fim='22')
quadra2 = Quadra(nome='Quadra 2', hora_inicio='10', hora_fim='22')
quadra3 = Quadra(nome='Quadra 3', hora_inicio='10', hora_fim='22')
quadra4 = Quadra(nome='Quadra 4', hora_inicio='10', hora_fim='22')

agenda = Agenda()

try:
    agendar = quadra1.agendar('2023-02-07', '10', '11')
    confirma = agenda.confirmar_reserva(cliente.nome, '2023-02-07', '10', '11')
except HorarioForaDoFuncionamento as e:
    print(e)



input()



cliente = Cliente(
    nome='Ricardo Martins',
    cpf='278.759.698-32',
    telefone='19 99999-8888',
    email='xxxxxx.xxxxxxxx@gmail.com'
)

try:
    agendar = quadra1.agendar('2023-02-07', '10', '11')
    confirma = agenda.confirmar_reserva(cliente.nome, '2023-02-07', '10', '11')
except HorarioForaDoFuncionamento as e:
    print(e)

for agendamento in agenda.reservas:
    print(agendamento)























# while True:
#     try:
#         data = input('Informe a data (yyyy-mm-dd): ')
#         hora_inicio = input('Informe a hora de início: ')
#         hora_fim = input('Informe a hora de término: ')
#         disponivel = agenda.verificar_disponibilidade(data, hora_inicio, hora_fim)
#         if disponivel == []:
#             print("Nenhuma quadra disponível")
#         else:
#             print("Quadras disponíveis nesse horário: \n")
#             for quadra in disponivel:
#                 print(quadra.nome)
#             break
#     except HorarioForaDoFuncionamento as e:
#         print('Erro: ' + str(e))