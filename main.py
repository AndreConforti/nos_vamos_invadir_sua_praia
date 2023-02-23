import sys
import json
from classes.agenda import Agenda
from pydantic import BaseModel
from classes.reserva import Reserva
from classes.cliente import Cliente

# Cria a instância de Agenda
agenda = Agenda()

# Opção 1 = Verificar Quadra Disponível
def quadra_disponivel():
    # Parâmetros
    data=input('Digite a data no formato yyyy-mm-dd:')
    hora_ini=input('Informe horário de início:')
    duracao=input('Informe duração desejada (1 ou 3):')

    # Chamada
    quadras = agenda.quadra_disponivel (data, hora_ini, duracao)
    
    # Retorno
    print('----------------------------------------------------------------')
    if not quadras:            
        print('Nenhuma quadra disponível neste horário!')
    else:
        for quadra in quadras:
            print ('Quadras disponíveis:', quadra.nome)
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')

# Opção 2 = Consultar Agendamentos Cliente
def reservas_cliente():
    # Parâmetros
    nome=input('Informe o nome do cliente:')

    # Chamada
    reservas = agenda.reservas_cliente (nome)

    # Retorno
    print('----------------------------------------------------------------')
    if not reservas:
        print('Nenhuma reserva localizada!')
    else:
        #for reserva in reservas:
        #    print ('Reservas realizadas:', reserva)
        count_res = 1
        for reserva in reservas:
            print('----------------------------------------------------------------')
            print (f'Reserva {count_res}:')
            print(f'{reserva.quadra.nome} - dia {reserva.data}, das {reserva.hora_inicio}h até {reserva.hora_fim()}h, {reserva.duracao} hora(s).')
            reserva_dict = vars(reserva.cliente)
            print(f'''Cliente: {json.dumps(reserva_dict, indent=4)}''')
            count_res += 1
    print('----------------------------------------------------------------')
    print('----------------------------------------------------------------')

# Opção 3 = Reservar quadra para cliente
def agendar():
    # Parâmetros
    print('Dados Cliente:')
    nome=input('Informe o nome do cliente:')
    cpf=input('Informe o CPF do cliente:')
    telefone=input('Informe o telefone do cliente:')
    email=input('Informe o e-mail do cliente:')
    print('Dados do Agendamento:')
    data=input('Digite a data no formato yyyy-mm-dd:')
    hora_ini=input('Informe horário de início:')
    duracao=input('Informe duração desejada (1 ou 3):')
    try:    # Adiciona cliente validando os valores informados
        cliente = Cliente(nome=nome, cpf=cpf, telefone=telefone, email=email)
    except ValueError as e:
        print(str(e))
        return

    # Chamada
    quadra = agenda.agendar(cliente=cliente, data=data, hora_ini=hora_ini, duracao=duracao)

    # Retorno
    if quadra:
        print(f'Quadra [{quadra.nome}] reservada com sucesso!')
    else:
        print(f'Nenhuma quadra disponível neste horário')

def menu_option(opt):
    
    if not isinstance(opt, int):
        return 0
    
    if opt == 1:
        quadra_disponivel()

    if opt == 2:
        reservas_cliente()

    if opt == 3:
        agendar()

    return opt


# Verifica se há alguma opção inicial selecionada
if len(sys.argv) == 1:
    opt = 0
    print ('Olá! Parece que você não escolheu nenhuma opção válida!')
else:
    opt = sys.argv[1]



while (opt != 7):

    opt = menu_option(opt)
    
    # Menu:
    print ('''
    Temos as seguintes opções:

    1 - Consultar Disponibilidade (Informar: Quadra, Data/Hora, Duração) - retornará Hora e Cliente se já houver reserva
    2 - Consultar Agendamento Cliente (Informar: Cliente) - retornará quadra, data e horário agendado
    3 - Agendar (Informar: Cliente, Quadra, Data/Hora, Duração) - retornará sucesso ou hora e cliente ocupado
    4 - Cancelar (Informar: Cliente, Quadra, Data/Hora) - retornará sucesso dos horários cancelados ou negativa
    5 - Pagamento (Informa: Cliente, Quadra, Data/Hora) - retornará sucesso da operação
    6 - Debito (Informar: Cliente, Periodo) - retornará o valor do débito
    7 - Sair

        ''')

    opt = int(input("Digite sua opção: "))

    
   

print ('Obrigado por utilizar nossos serviços!')





    


    